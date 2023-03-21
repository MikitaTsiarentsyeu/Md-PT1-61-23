time = {1: ['один', 'первого'], 2: ['два', 'второго'], 3: ['три', 'третьего'], 4: ['четыре', 'четвертого'], 5: ['пять', 'пятого'], 6: ['шесть', 'шестого'], 7: [
    'семь', 'седьмого'], 8: ['восемь', 'восьмого'], 9: ['девять', 'девятого'], 10: ['десять', 'десятого'], 11: ['одиннадцать', 'одиннадцатого'], 12: ['двенадцать', 'двенадцатого']}

input_time = input("Enter the time hh:mm \n")
input_time = input_time.split(':')
if int(input_time[0]) < 10:
    input_time[0] = '0' + input_time[0]
if int(input_time[1]) < 10:
    input_time[1] = '0' + input_time[1]

hour = int(input_time[0])
min = int(input_time[1])

if hour > 12:
    hour -= 12
if min == 0:
    if hour == 0:
        print(f"{input_time[0]}:{input_time[1]} - {time[12][0]} часов ровно")
    elif hour == 1:
        print(f"{input_time[0]}:{input_time[1]} - {time[hour][0]} час ровно")
    elif hour >= 2 and hour <= 4:
        print(f"{input_time[0]}:{input_time[1]} - {time[hour][0]} часа ровно")
    else:
        print(f"{input_time[0]}:{input_time[1]} - {time[hour][0]} часов ровно")
elif hour >= 12:
    hour -= 12
if min < 30:
    if min == 1:
        print(
            f"{input_time[0]}:{input_time[1]} - {time[min][0][:2]}на минута {time[hour+1][1]}")
    elif min == 2:
        print(
            f"{input_time[0]}:{input_time[1]} - {time[min][0][:2]}е минуты {time[hour+1][1]}")
    elif min >= 3 and min <= 4:
        print(
            f"{input_time[0]}:{input_time[1]} - {time[min][0]} минуты {time[hour+1][1]}")
    elif min >= 5 and min <= 10:
        print(
            f"{input_time[0]}:{input_time[1]} - {time[min][0]} минут {time[hour+1][1]}")
    elif min == 11 or min == 13:
        print(
            f"{input_time[0]}:{input_time[1]} - {time[min-10][0]}надцать минут {time[hour+1][1]}")
    elif min >= 14 and min <= 19:
        print(
            f"{input_time[0]}:{input_time[1]} - {time[min-10][0][:-1]}надцать минут {time[hour+1][1]}")
    elif min == 12:
        print(
            f"{input_time[0]}:{input_time[1]} - {time[min-10][0][:2]}енадцать минут {time[hour+1][1]}")
    elif min == 20:
        print(
            f"{input_time[0]}:{input_time[1]} - двадцать минут {time[hour+1][1]}")
    elif min == 21:
        print(
            f"{input_time[0]}:{input_time[1]} - двадцать {time[min-20][0][:2]}на минута {time[hour+1][1]}")
    elif min == 22:
        print(
            f"{input_time[0]}:{input_time[1]} - двадцать {time[min-20][0][:2]}е минуты {time[hour+1][1]}")
    elif min >= 23 and min <= 24:
        print(
            f"{input_time[0]}:{input_time[1]} - двадцать {time[min-20][0]} минуты {time[hour+1][1]}")
    elif min >= 25 and min <= 29:
        print(
            f"{input_time[0]}:{input_time[1]} - двадцать {time[min-20][0]} минут {time[hour+1][1]}")
if min == 30:
    print(
        f"{input_time[0]}:{input_time[1]} - половина {time[hour+1][1]}")
if min > 30 and min < 45:
    if min == 31:
        print(
            f"{input_time[0]}:{input_time[1]} - тридцать {time[min-30][0][:2]}на минута {time[hour+1][1]}")
    elif min == 32:
        print(
            f"{input_time[0]}:{input_time[1]} - тридцать {time[min-30][0][:2]}е минуты {time[hour+1][1]}")
    elif min >= 33 and min <= 34:
        print(
            f"{input_time[0]}:{input_time[1]} - тридцать {time[min-30][0]} минуты {time[hour+1][1]}")
    elif min >= 35 and min < 40:
        print(
            f"{input_time[0]}:{input_time[1]} - тридцать {time[min-30][0]} минут {time[hour+1][1]}")
    elif min == 41:
        print(
            f"{input_time[0]}:{input_time[1]} - сорок {time[min-40][0][:2]}на минута {time[hour+1][1]}")
    elif min == 42:
        print(
            f"{input_time[0]}:{input_time[1]} - сорок {time[min-40][0][:2]}е минуты {time[hour+1][1]}")
    elif min >= 43 and min <= 44:
        print(
            f"{input_time[0]}:{input_time[1]} - сорок {time[min-40][0]} минуты {time[hour+1][1]}")
    else:
        print(
            f"{input_time[0]}:{input_time[1]} - сорок минут {time[hour+1][1]}")
if min >= 45:
    min = 60 - min
    if min == 1:
        print(
            f"{input_time[0]}:{input_time[1]} - без {time[min][0][:2]}ной минуты {time[hour+1][0]}")
    elif min == 2:
        print(
            f"{input_time[0]}:{input_time[1]} - без {time[min][0][:2]}ух минут {time[hour+1][0]}")
    elif min == 3 or min == 4:
        print(
            f"{input_time[0]}:{input_time[1]} - без {time[min][0][:-1]}ёх минут {time[hour+1][0]}")
    elif min == 8:
        print(
            f"{input_time[0]}:{input_time[1]} - без {time[min][0][:3]}ьми минут {time[hour+1][0]}")
    elif min >= 5 and min <= 10:
        print(
            f"{input_time[0]}:{input_time[1]} - без {time[min][0][:-1]}и минут {time[hour+1][0]}")
    elif min >= 14 and min <= 15:
        print(
            f"{input_time[0]}:{input_time[1]} - без {time[min-10][0][:-1]}надцати минут {time[hour+1][0]}")
    elif min == 11:
        print(
            f"{input_time[0]}:{input_time[1]} - без {time[min-10][0]}надцати минут {time[hour+1][0]}")
    elif min == 12:
        print(
            f"{input_time[0]}:{input_time[1]} - без {time[min-10][0][:-1]}енадцати минут {time[hour+1][0]}")
    elif min == 13:
        print(
            f"{input_time[0]}:{input_time[1]} - без {time[min-10][0]}надцати минут {time[hour+1][0]}")
