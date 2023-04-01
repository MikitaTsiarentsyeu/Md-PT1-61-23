h_dict1 = {0: ['ноль часов', 'первого', 'час'], 1: ['один час', 'второго', 'два'], 2: ['два часа', 'третьего', 'три'],
           3: ['три часа', 'четвертого', 'четыре'], 4: ['четыре часа', 'пятого', 'пять'],
           5: ['пять часов', 'шестого', 'шесть'],
           6: ['шесть часов', 'седьмого', 'семь'], 7: ['семь часов', 'восьмого', 'восемь'],
           8: ['восемь часов', 'девятого', 'девять'],
           9: ['девять часов', 'десятого', 'десять'], 10: ['десять часов', 'одиннадцатого', 'одиннадцать'],
           11: ['одиннадцать часов', 'двенадцатого', 'двенадцать'], 12: ['двенадцать часов', 'первого', 'час']
           }

m_dict1 = {0: 'ровно', 1: ['одна', 'одной'], 2: ['две', 'двух'], 3: ['три', 'трех'], 4: ['четыре', 'четырех'],
           5: ['пять', 'пяти'], 6: ['шесть', 'шести'], 7: ['семь', 'семи'], 8: ['восемь', 'восьми'],
           9: ['девять', 'девяти'], 10: ['десять', 'десяти'], 11: ['одиннадцать', 'одиннадцати'],
           12: ['двенадцать', 'двенадцати'], 13: ['тринадцать', 'тринадцати'], 14: ['четырнадцать', 'четырнадцати'],
           15: ['пятнадцать', 'пятнадцати'], 16: ['шестнадцать'], 17: ['семнадцать'], 18: ['восемнадцать'],
           19: ['девятнадцать'], 20: 'двадцать', 30: 'тридцать', 40: 'сорок'
           }
m_list1 = ['минут', 'минуты', 'минута']

# users input:
user_inp = input("Please input your time in HH:MM format:\n")
user_inp = user_inp.replace(' ', '').split(':')

# users input validation:
if user_inp[0].isnumeric():
    hours = int(user_inp[0])
else:
    print("Incorrect Hours value")
    exit()
if user_inp[1].isnumeric():
    min = int(user_inp[1])
else:
    print("Incorrect Minutes value")
    exit()

if hours < 0 or hours > 23:
    print('Hours value should be in 0-23 interval')
    exit()
elif 0 <= hours <= 12:
    hours = hours
elif 12 < hours <= 23:
    hours = hours - 12

if min == 0:
    print(f'{h_dict1[hours][0]} {m_dict1[min]}')
elif min == 30:
    print(f'половина {h_dict1[hours][1]}')
elif min < 30 or 30 < min < 45:
    if min == 1:
        print(f'{m_dict1[min][0]} {m_list1[2]} {h_dict1[hours][1]}')
    elif 1 < min < 5:
        print(f'{m_dict1[min][0]} {m_list1[1]} {h_dict1[hours][1]}')
    elif 5 <= min < 20:
        print(f'{m_dict1[min][0]} {m_list1[0]} {h_dict1[hours][1]}')
    else:
        min_1 = list(user_inp[1])
        # print(min_1)
        min_2 = int(min_1[1])
        # print(min_2)
        if 1 < min_2 < 5:
            dif = min - min_2
            # print(dif)
            print(f'{m_dict1[dif]} {m_dict1[min_2][0]} {m_list1[1]} {h_dict1[hours][1]}')
        elif min_2 == 1 and min > 20:
            dif = min - 1
            # print(dif)
            print(f'{m_dict1[dif]} {m_dict1[1][0]} {m_list1[2]} {h_dict1[hours][1]}')
        elif min_2 == 0:
            print(f'{m_dict1[min]} {m_list1[0]} {h_dict1[hours][1]}')
        elif 4 < min_2 <10:
            dif = min - min_2
            print(f'{m_dict1[dif]} {m_dict1[min_2][0]} {m_list1[0]} {h_dict1[hours][1]}')
elif 45<= min <60:
    min_2 = 60-min
    if min_2 ==1:
        print(f'без {m_dict1[min_2][1]} {m_list1[1]} {h_dict1[hours][2]}')
    else:
        print(f'без {m_dict1[min_2][1]} {m_list1[0]} {h_dict1[hours][2]}')
else:
    print('Invalid input. Try again')
