hours_dict = {}

hours_dict.update(dict.fromkeys([1, 13], ('Один час', 'второго', 'два')))
hours_dict.update(dict.fromkeys([2, 14], ('Два часа', 'третьего', 'три')))
hours_dict.update(dict.fromkeys([3, 15], ('Три часа', 'четвертого', 'четыре')))
hours_dict.update(dict.fromkeys([4, 16], ('Четыре часа', 'пятого', 'пять')))
hours_dict.update(dict.fromkeys([5, 17], ('Пять часов', 'шестого', 'шесть')))
hours_dict.update(dict.fromkeys([6, 18], ('Шесть часов', 'седьмого', 'семь')))
hours_dict.update(dict.fromkeys([7, 19], ('Семь часов', 'восьмого', 'восемь')))
hours_dict.update(dict.fromkeys([8, 20], ('Восемь часов', 'девятого', 'девять')))
hours_dict.update(dict.fromkeys([9, 21], ('Девять часов', 'десятого', 'десятого')))
hours_dict.update(dict.fromkeys([10, 22], ('Десять часов', 'одиннадцатого', 'одиннадцать')))
hours_dict.update(dict.fromkeys([11, 23], ('Одиннадцать часов', 'двенадцатого', 'двенадцать')))
hours_dict.update(dict.fromkeys([12, 0], ('Двенадцать часов', 'первого', 'час')))

minutes_dict = {1: ('Одна минута', 'Без одной минуты'), 2: ('Две минуты', 'Без двух минут'),
                3: ('Три минуты', 'Без трех минут'), 4: ('Четыре минуты', 'Без четырех минут'),
                5: ('Пять минут', 'Без пяти минут'), 6: ('Шесть минут', 'Без шести минут'),
                7: ('Семь минут', 'Без семи минут'), 8: ('Восемь минут', 'Без восьми минут'),
                9: ('Девять минут', 'Без девяти минут'), 10: ('Десять минут', 'Без десяти минут'),
                11: ('Одиннадцать минут', 'Без одиннадцати минут'), 12: ('двенадцать минут', 'Без двенадцати минут'),
                13: ('Тринадцать минут', 'Без тринадцати минут'), 14: ('Четырнадцать минут', 'Без четырнадцати минут'),
                15: ('Пятнадцать минут', 'Без пятнадцати минут'), 16: 'Шестнадцать минут',
                17: 'Семнадцать минут', 18: 'Восемнадцать минут', 19: 'Девятнадцать минут',
                20: 'Двадцать минут', 21: 'Двадцать одна минута', 22: 'Двадцать две минуты',
                23: 'Двадцать три минуты', 24: 'Двадцать четыре минуты', 25: 'Двадцать пять минут',
                26: 'Двадцать шесть минут', 27: 'Двадцать семь минут', 28: 'Двадцать восемь минут',
                29: 'Двадцать девять минут', 30: 'Половина', 31: 'Тридцать одна минута',
                32: 'Тридцать две минуты', 33: 'Тридцать три минуты', 34: 'Тридцать четыре минуты',
                35: 'Тридцать пять минут', 36: 'Тридцать шесть минут', 38: 'Тридцать восемь минут',
                39: 'Тридцать девять минут', 40: 'Сорок минут', 41: 'Сорок одна минута',
                42: 'Сорок две минуты', 43: 'Сорок три минуты', 44: 'Сорок четыре минуты'}

time = input('Enter the time (hh:mm): ')

if ':' in time and time.count(':') == 1:
    time_values = time.split(':')
    if time_values[0].isdigit() and time_values[1].isdigit():
        hours = int(time_values[0])
        minutes = int(time_values[1])

        if hours > 24 or hours < 0 or minutes > 60 or minutes < 0:
            print('Wrong input! Hours should be 0-24, minutes should be 0-60.')
            exit(1)

        if minutes == 0:
            print(f'{hours}:00 - {hours_dict[hours][0]} ровно')
        elif minutes <= 15:
            print(f'{hours}:{minutes} - {minutes_dict[minutes][0]} {hours_dict[hours][1]}')
        elif minutes <= 29:
            print(f'{hours}:{minutes} - {minutes_dict[minutes]} {hours_dict[hours][1]}')
        elif minutes == 30:
            print(f'{hours}:{minutes} - Половина {hours_dict[hours][1]}')
        elif minutes <= 45:
            print(f'{hours}:{minutes} - {minutes_dict[minutes]} {hours_dict[hours][1]}')
        else:
            minutes_left = 60 - minutes
            print(f'{hours}:{minutes} - {minutes_dict[minutes_left][1]} {hours_dict[hours][2]}')
    else:
        print('Wrong input!')
else:
    print('Wrong input!')
