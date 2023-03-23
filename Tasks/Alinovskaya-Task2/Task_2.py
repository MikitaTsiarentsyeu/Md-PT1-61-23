information_from_user = input("Enter time in format hh:mm");

information_from_user_split = information_from_user.split(":");
hours = int(information_from_user_split[0]);
minutes = int(information_from_user_split[1]);

dictionary_hours_num = {13:1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11, 00:12, 24:12};
dictionary_hours = {1:["час","первого"], 2:["два", "второго"], 3:["три", "третьего"], 4:["четыре", "четвертого"], 
                    5:["пять", "пятого"], 6:["шесть", "шестого"], 7:["семь","седьмого"], 8:["восемь","восьмого"], 
                    9:["девять","девятого"], 10:["десять","десятого"], 11:["одинадцать","одинадцатого"], 12:["двенадцать","двенадцатого"]};

dictionary_minutes = {1: ["одна минута", "без одной минуты"], 2: ["две минуты", "без двух минут"],
                      3: ["три минуты", "без трех минут"], 4: ["четыре минуты", "без четырех минут"],
                      5: ["пять минут", "без пяти минут"], 6: ["шесть минут", "без шести минут"],
                      7: ["семь минут", "без семи минут"], 8: ["Восемь минут", "без восьми минут"],
                      9: ["девять минут", "без девяти минут"], 10: ["десять минут", "без десяти минут"],
                      11: ["одиннадцать минут", "без одиннадцати минут"], 12: ["двенадцать минут", "без двенадцати минут"],
                      13: ["тринадцать минут", "без тринадцати минут"], 14: ["четырнадцать минут", "без четырнадцати минут"],
                      15: ["пятнадцать минут", "без пятнадцати минут"], 16: ["шестнадцать минут", "без шестнадцати минут"],
                      17: ["семнадцать минут", "без семнадцати минут"], 18: ["Восемнадцать минут", "без восемнадцати минут"],
                      19: ["девятнадцать минут", "без девятнадцати минут"], 20: ["двадцать минут", "без двадцати минут"], 
                      21: "двадцать одна минута", 22: "двадцать две минуты", 23: "двадцать три минуты",
                      24: "двадцать четыре минуты", 25: "двадцать пять минут",26: "двадцать шесть минут", 
                      27: "двадцать семь минут", 28: "двадцать восемь минут",29: "двадцать девять минут", 
                      30: "половина", 31: "тридцать одна минута", 32: "тридцать две минуты", 
                      33: "тридцать три минуты", 34: "тридцать четыре минуты", 35: "тридцать пять минут", 
                      36: "тридцать шесть минут", 37: "тридцать пять минут",  38: "тридцать восемь минут", 39: "тридцать девять минут",
                      40: "сорок минут", 41: "сорок одна минута", 42: "сорок две минуты", 43: "сорок три минуты", 
                      44: "сорок четыре минуты"}
 
if minutes == 00:
    if hours in dictionary_hours:
        if hours < 2:
            print(f"{dictionary_hours[hours][0]} ровно");
        elif hours < 5:
            print(f"{dictionary_hours[hours][0]} часа ровно");
        else:
            print(f"{dictionary_hours[hours][0]} часов ровно");
    elif hours in dictionary_hours_num :
        if hours < 5:
            print(f"{dictionary_hours[dictionary_hours_num[hours]][0]} часа ровно");
        else:
            print(f"{dictionary_hours[dictionary_hours_num[hours]][0]} часов ровно");
elif minutes < 30:
    if minutes > 20:
            if hours in dictionary_hours:
                if hours == 12:
                    print(f"{dictionary_minutes[minutes]} {dictionary_hours[1][1]}");
                else:
                    print(f"{dictionary_minutes[minutes]} {dictionary_hours[hours + 1][1]}");
            elif hours in dictionary_hours_num:
                if hours == 0:
                    print(f"{dictionary_minutes[minutes]} {dictionary_hours[hours + 1][1]}");
                else:
                    print(f"{dictionary_minutes[minutes]} {dictionary_hours[dictionary_hours_num[hours + 1]][1]}");
    else:
        print(hours);
        if hours in dictionary_hours:
            if hours == 12:
                print(f"{dictionary_minutes[minutes][0]} {dictionary_hours[1][1]}");
            else:
                print(f"{dictionary_minutes[minutes][0]} {dictionary_hours[hours + 1][1]}");
        elif hours in dictionary_hours_num:
            if hours == 0:
                print(f"{dictionary_minutes[minutes][0]} {dictionary_hours[hours + 1][1]}");
            elif hours == 12:
                    print(f"{dictionary_minutes[minutes]} {dictionary_hours[1][1]}");
            else:
                print(f"{dictionary_minutes[minutes][0]} {dictionary_hours[dictionary_hours_num[hours + 1]][1]}");
elif minutes == 30:
    if hours in dictionary_hours:
        if hours == 12:
            print(f"половина {dictionary_hours[1][1]}");
        else:
            print(f"половина {dictionary_hours[hours + 1][1]}");
    elif hours in dictionary_hours_num:
        if hours == 0:
            print(f"половина {dictionary_hours[hours + 1][1]}");  
        else:
            print(f"половина {dictionary_hours[dictionary_hours_num[hours + 1]][1]}");  
elif minutes > 30 and minutes < 45:
    if hours in dictionary_hours:
        if hours == 12:
            print(f"{dictionary_minutes[minutes]} {dictionary_hours[1][1]}");
        else:    
            print(f"{dictionary_minutes[minutes]} {dictionary_hours[hours+1][1]}");
    elif hours in dictionary_hours_num:
        if hours == 0:
            print(f"{dictionary_minutes[minutes]} {dictionary_hours[hours + 1][1]}"); 
        else:
            print(f"{dictionary_minutes[minutes]} {dictionary_hours[dictionary_hours_num[hours + 1]][1]}");
elif minutes >= 45 and minutes < 60:
    if hours in dictionary_hours:
        if hours == 12:
            print(f"{dictionary_minutes[60-minutes][1]} {dictionary_hours[1][0]}");
        else:    
            print(f"{dictionary_minutes[60-minutes][1]} {dictionary_hours[hours + 1][0]}");
    elif hours in dictionary_hours_num:
        if hours == 0:
            print(f"{dictionary_minutes[60-minutes][1]} {dictionary_hours[hours +1][1]}");
        else:
            print(f"{dictionary_minutes[60-minutes][1]} {dictionary_hours[dictionary_hours_num[hours +1]][1]}")
else:
     print("wrong input time format");


# Implement a text output of the time entered from the console (the user should input data in the format hh:mm).

# Show the responses to the user in Russian according to the rules listed below:

# min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
# min == 30: половина такого-то (15:30 - половина четвёртого)
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
# min >= 45 без min такого-то (08:54 - без шести минут девять)