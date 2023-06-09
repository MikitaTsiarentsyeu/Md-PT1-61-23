time = input("Input time in format hh:mm: \n")
time = time.replace(' ', '')
part = time.split(':')
print(part)

#валидация
if part[0].isdigit():
    h = int(part[0])
if 0 <= h <= 24:
    h = int(part[0])
else:
    print("invalid format of entered time in hh")

if part[1].isdigit():
    m = int(part[1])
if 0 <= m <= 60:
    m = int(part[1])
else:
    print("invalid format of entered time in mm")

#словарь
d = {1:["один", "первого", "одной"], 2:["два", "второго", "двух"], 3:["три", "третьего", "трёx"],
    4:["четыре", "четвертого", "четырёх"], 5:["пять", "пятого", "пяти"], 6:["шесть", "шестого", "шести"],
    7:["семь", "седьмого", "семи"], 8:["восемь", "восьмого", "восьми"], 9:["девять", "девятого", "девяти"],
    10:["десять", "десятого", "десяти"], 11:["одиннадцать", "одиннадцатого", "одиннадцати"], 12:["двенадцать", "двенадцатого", "двенадцати"],
    13:["тринадцать", "тринадцатого", "тринадцати"], 14:["четырнадцать", "четырнадцатого", "четырнадцати"], 15:["пятнадцать", "пятнадцатого", "пятнадцати"],
    16: ["шестнадцать"], 17: ["семнадцать"], 18:["восемнадцать"], 19: ["девятнадцать"], 20: ["двадцать"], 21: ["двадцать один"], 22: ["двадцать два"], 23: ["двадцать три"],
    24: ["двадцать четыре"], 25: ["двадцать пять"], 26: ["двадцать шесть"], 27: ["двадцать семь"], 28: ["двадцать восемь"], 29: ["двадцать девять"], 30: ["тридцать"],
    31: ["тридцать один"], 32: ["тридцать два"], 33: ["тридцать три"], 34: ["тридцать четыре"], 35: ["тридцать пять"], 36: ["тридцать шесть"],
    37: ["тридцать семь"], 38: ["тридцать восемь"], 39: ["тридцать девять"], 40: ["сорок"], 41: ["сорок один"], 42: ["сорок два"], 43: ["сорок три"],
    44: ["сорок четыре"], 45:["сорок пять"]}

#min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
if m == 0:
    if h == 1:
        h_print = d[h]
        print(f'{h_print[0]} час ровно')
    if 2 <= h <= 4:
        print(f'{h_print[0]} часа ровно')
    if h == 13:
        h_print = d[h]
        d[13] = d[1]
        h_print = d[h]
        print(f'{h_print[0]} час ровно')
    if 14 <= h <= 16:
        h_print = d[h]
        d[14] = d[2]
        d[15] = d[3]
        d[16] = d[4]
        h_print = d[h]
        print(f'{h_print[0]} часа ровно')
    if 17 <= h <= 24:
        h_print = d[h]
        d[17] = d[5]
        d[18] = d[6]
        d[19] = d[7]
        d[20] = d[8]
        d[21] = d[9]
        d[22] = d[10]
        d[23] = d[11]
        d[24] = d[12]
        h_print = d[h]
        print(f'{h_print[0]} часов ровно')

# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
if 0 < m < 30:
    if 13 <= h <=24:
        m_print = d[m]
        h = h + 1
        h_print = d[h]
        d[13] = d[1]
        d[14] = d[2]
        d[15] = d[3]
        d[16] = d[4]
        d[17] = d[5]
        d[18] = d[6]
        d[19] = d[7]
        d[20] = d[8]
        d[21] = d[9]
        d[22] = d[10]
        d[23] = d[11]
        d[24] = d[12]
        h_print = d[h]
        print(f'{m_print[0]} минут {h_print[1]}')
    else:
        m_print = d[m]
        h = h + 1
        h_print = d[h]
        print(f'{m_print[0]} минут {h_print[1]}')

# min == 30: половина такого-то (15:30 - половина четвёртого)
if m == 30:
    if 13 <= h <=24:
        h = h + 1
        h_print = d[h]
        d[13] = d[1]
        d[14] = d[2]
        d[15] = d[3]
        d[16] = d[4]
        d[17] = d[5]
        d[18] = d[6]
        d[19] = d[7]
        d[20] = d[8]
        d[21] = d[9]
        d[22] = d[10]
        d[23] = d[11]
        d[24] = d[12]
        h_print = d[h]
        print(f'половина {h_print[1]}')
    else:
        h = h + 1
        h_print = d[h]
        print(f'половина {h_print[1]}')

# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
if 30 < m < 45:
    if 13 <= h <=24:
        m_print = d[m]
        h = h + 1
        h_print = d[h]
        d[13] = d[1]
        d[14] = d[2]
        d[15] = d[3]
        d[16] = d[4]
        d[17] = d[5]
        d[18] = d[6]
        d[19] = d[7]
        d[20] = d[8]
        d[21] = d[9]
        d[22] = d[10]
        d[23] = d[11]
        d[24] = d[12]
        h_print = d[h]
        print(f'{m_print[0]} минут {h_print[1]}')
    else:
        m_print = d[m]
        h = h + 1
        h_print = d[h]
        print(f'{m_print[0]} минут {h_print[1]}')

# min >= 45 без min такого-то (08:54 - без шести минут девять)
if m >= 45:
    if 13 <= h <=24:
        m = 60 - m
        m_print = d[m]
        h = h + 1
        h_print = d[h]
        d[13] = d[1]
        d[14] = d[2]
        d[15] = d[3]
        d[16] = d[4]
        d[17] = d[5]
        d[18] = d[6]
        d[19] = d[7]
        d[20] = d[8]
        d[21] = d[9]
        d[22] = d[10]
        d[23] = d[11]
        d[24] = d[12]
        h_print = d[h]
        if m == 1:
            print(f'без {m_print[2]} минуты {h_print[0]}')
            exit ()
        print(f'без {m_print[2]} минут {h_print[0]}')
    else:
        m = 60 - m
        m_print = d[m]
        h = h + 1
        h_print = d[h]
        print(f'без {m_print[2]} минут {h_print[0]}')
