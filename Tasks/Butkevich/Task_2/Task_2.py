# Implement a text output of the time entered from the console (the user should input data in the format hh:mm).
#
# Show the responses to the user in Russian according to the rules listed below:
#
# min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
# min == 30: половина такого-то (15:30 - половина четвёртого)
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
# min >= 45 без min такого-то (08:54 - без шести минут девять)
print("If you want to start, press 1")
print("If you want to end, press 2\n")
while True:
    user_input = input()
    if user_input != "2":
        time_user = input()
        if len(time_user) == 5 and time_user[2] == ":" and time_user[0].isdigit() == True and time_user[
            1].isdigit() == True \
                and time_user[3].isdigit() == True and time_user[4].isdigit() == True and 0 <= int(
            time_user[0:2]) <= 24 and 0 \
                <= int(time_user[3:]) <= 60:
            d_rovno = {"00": ["двенадцать часов", "первого"],
                       "01": ["один час", "второго", "одна минута", "без одной минуты"],
                       "02": ["два часа", "третьего", "две минуты", "без двух минут"],
                       "03": ["три часа", "четвертого", "три минуты", "без трех минут"],
                       "04": ["четыре часа", "пятого", "четыре минут", "без четырех минут"],
                       "05": ["пять часов", "шестого", " пять минут", "без пяти минут"],
                       "06": ["шесть часов", "седьмого", "шесть минут", "без шести минут"],
                       "07": ["семь часов", "восьмого", "семь минут", "без семи минут"],
                       "08": ["восьмь часов", "девятотого", "восемь минут", "без восьми минут"],
                       "09": ["девять часов", "десятого", "девять минут", "без девяти минут"],
                       "10": ["десять часов", "одинадцатого", "десять минут", "без десяти минут"],
                       "11": ["одинадцать часов", "двенадцаого", "одинадцать минут", "без одинадцати минут"],
                       "12": ["двенадцать часов", "первого", "двенадцать минут", "без двенадцати минут"],
                       "13": ["один час", "второго", "тринадцать минут", "без тринадцати минут"],
                       "14": ["два часа", "третьего", "четырнадцать минут", "без четырнадцати минут"],
                       "15": ["три часа", "четвертого", "пятнадцать минут", "без пятнадцати минут"],
                       "16": ["четыре часа", "пятого", "шестнадцать минут"],
                       "17": ["пять часов", "шестого", "семнадцать минут"],
                       "18": ["восемь часов", "седьмого", "Восемнадцать минут"],
                       "19": ["семь часов", "восьмого", "девятнадцать минут"],
                       "20": ["восемь часов", "девятого", "двадцать минут"],
                       "21": ["девять часов", "десятого", "двадцать одна минута"],
                       "22": ["десять часов", "одинадцатого", "двадцать две минуты"],
                       "23": ["одинадцать часов", "двенадцатого", "двадцать три минуты"],
                       "24": ["двенадцать часов", "первого", "двадцать четыре минуты"],
                       "25": ["", "двадцать пять минут"],
                       "26": ["", "двадцать шесть минут"],
                       "27": ["", "двадцать семь минут"],
                       "28": ["", "двадцать восемь минут"],
                       "29": ["", "двадцать девять минут"],
                       "31": ["", "тридцать одна минута"],
                       "32": ["", "тридцать две минуты"],
                       "33": ["", "тридцать три минуты"],
                       "34": ["", "тридцать четыре минуты"],
                       "35": ["", "тридцать пять минут"],
                       "36": ["", "тридцать шесть минут"],
                       "37": ["", "тридцать пять минут"],
                       "38": ["", "тридцать восемь минут"],
                       "39": ["", "тридцать девять минут"],
                       "40": ["", "сорок минут"],
                       "41": ["", "сорок одна минута"],
                       "42": ["", "сорок две минуты", ],
                       "43": ["", "сорок три минуты", ],
                       "44": ["", "сорок четыре минуты"]

                       }
            for k, d in d_rovno.items():
                if time_user[3:] == "00":
                    if time_user[0:2] == k:
                        print(f"{d[0]} ровно")
                elif time_user[3:] == "30":
                    if time_user[0:2] == k:
                        print(f"половина {d[1]}")
                elif 0 < int(time_user[3:]) < 30 and int(time_user[3:]) == int(k):
                    if 0 < int(time_user[3:]) < 13:
                        l = []
                        l.append(d[1])
                        for a, b in d_rovno.items():
                            if a == time_user[0:2]:
                                l.append(b[1])
                        print(*l)
                    elif 12 < int(time_user[3:]) < 30:
                        l = []
                        l.append(d[2])
                        for a, b in d_rovno.items():
                            if a == time_user[0:2]:
                                l.append(b[1])
                        print(*l)
                elif 30 < int(time_user[3:]) < 45 and int(time_user[3:]) == int(k):
                    l = []
                    l.append(d[1])
                    for a, b in d_rovno.items():
                        if a == time_user[0:2]:
                            l.append(b[1])
                    print(*l)
                elif 44 < int(time_user[3:]) < 60 and abs(int(time_user[3:]) - 60) == int(k):
                    l = []
                    l.append(d[3])
                    for a, b in d_rovno.items():
                        if int(a) == int(time_user[0:2]) + 1:
                            l.append(b[0])
                    print(*l)
        else:
            print(f"{time_user} is not the correct input")

    else:
        print("The end")
        break
