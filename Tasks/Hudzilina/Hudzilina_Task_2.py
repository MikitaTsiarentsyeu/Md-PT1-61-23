
hours = {0:['ноль часов', 'первого', 'час'], 1:['один час', 'второго',
            'два'], 2:['два часа', 'третьего', 'три'], 3:['три часа', 
            'четвертого', 'четыре'], 4:['четыре часа', 'пятого', 'пять'],
            5:['пять часов', 'шестого', 'шесть'], 6:['шесть часов', 
            'седьмого', 'семь'], 7:['семь часов', 'восьмого', 'восемь'],
            8:['восемь часов', 'девятого', 'девять'], 9:['девять часов', 
            'десятого', 'десять'], 10:['десять часов', 'одиннадцатого', 
            'одиннадцать'], 11:['одиннадцать часов', 'двенадцатого', 
            'двенадцать'], 12:['двенадцать часов', 'первого', 'час']}

d_min = {1:['одна', 'одной'], 2:['две', 'двух'],
         3:['три', 'трех'], 4:['четыре', 'четырех'],
         5:['пять', 'пяти'], 6:['шесть', 'шести'],
         7:['семь', 'семи'], 8:['восемь', 'восьми'],
         9:['девять', 'девяти'], 10:['десять', 'десяти'], 
         11:['одиннадцать', 'одиннадцати'],
         12:['двенадцать', 'двенадцати'], 13:['тринадцать',
         'тринадцати'], 14:['четырнадцать', 'четырнадцати'], 
         15:['пятнадцать', 'пятнадцати'],
         16:'шестнадцать', 17:'семнадцать',
         18:'восемнадцать', 19:'девятнадцать',
         20:'двадцать', 30:'тридцать', 40:'сорок'}


call = input('Enter current time in format hh:mm: \n')
tm = call.split(':')
hour = int(tm[0])
min = int(tm[1])

def time_counter(min, hour):
    if min == 0:
        print(f'{call} - {hours[hour][0]} ровно')
    elif min == 30:
        print(f'{call} - половина {hours[hour][1]}')
    elif 0 < min < 30 or 30 < min < 45:
         if 4 < min < 20:
             print(f'{call} - {d_min[min][0]} минут {hours[hour][1]}')
         elif min == 1:
            print(f'{call} - {d_min[min][0]} минута {hours[hour][1]}')
         elif 1 < min < 5:
            print(f'{call} - {d_min[min][0]} минуты {hours[hour][1]}')
         else:
            min_1 = list(tm[1])
            min_2 = int(min_1[1])
            if 1 < min_2 < 5:
                dif = min - min_2
                print(f'{call} - {d_min[dif]} {d_min[min_2][0]} минуты {hours[hour][1]}')
            elif min_2 == 1 and min > 20:
                dif = min - 1
                print(f'{call} - {d_min[dif]} {d_min[1][0]} минута {hours[hour][1]}')
            elif min_2 == 0:
                print(f'{call} - {d_min[min]} минут {hours[hour][1]}')
            elif 4 < min_2 < 10:
                dif = min - min_2
                print(f'{call} - {d_min[dif]} {d_min[min_2][0]} минут {hours[hour][1]}')
    elif 45 <= min < 60:
        min_2 = 60 - min
        if min_2 == 1:
            print(f'{call} - без {d_min[min_2][1]} минуты {hours[hour][2]}')
        else:
            print(f'{call} - без {d_min[min_2][1]} минут {hours[hour][2]}')
    else:
        print("Incorrect data, please check the time.")

if hour < 0 or 23 < hour:
    print("Incorrect data, please check the time.")
elif 12 < hour < 24:
    hour = hour - 12
    time_counter(min, hour)
elif 0 <= hour <= 12:
    time_counter(min, hour)