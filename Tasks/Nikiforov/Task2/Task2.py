import re

d = {0:[[], ["ноль", "первого", "час"]], 1:[["одна"], ["один", "второго", "два"]], 2:[["две"], ["два", "третьего", "три"]], 
3:[["три"], ["три", "четвертого", "четыре"]], 4:[["четыре"], ["четыре", "пятого", "пять"]], 5:[["пять"], ["пять", "шестого", "шесть"]],
6:[["шесть"], ["шесть", "седьмого", "семь"]], 7:[["семь"], ["семь", "восьмого", "восемь"]], 8:[["восемь"], ["восемь", "девятого", "девять"]], 
9:[["девять"], ["девять", "десятого", "десять"]], 10:[["десять"], ["десять", "одиннадцатого", "одиннадцать"]], 
11:[["одиннадцать"], ["одиннадцать", "двенадцатого", "двенадцать"]], 12:[["двенадцать"], ["двенадцать", "первого", "час"]],
13:[["тринадцать"]], 14:[["четырнадцать"]], 15:[["пятнадцать"]], 16:[["шестнадцать"]], 17:[["семнадцать"]], 18:[["восемнадцать"]],
19:[["девятнадцать"]], 20:[["двадцать"]], 21:[["двадцать одна"]], 22:[["двадцать две"]], 23:[["двадцать три"]], 24:[["двадцать четыре"]],
25:[["двадцать пять"]], 26:[["двадцать шесть"]], 27:[["двадцать семь"]], 28:[["двадцать восемь"]], 29:[["двадцать девять"]], 30:[["тридцать"]],
31:[["тридцать одна"]], 32:[["тридцать две"]], 33:[["тридцать три"]], 34:[["тридцать четыре"]], 35:[["тридцать пять"]], 36:[["тридцать шесть"]],
37:[["тридцать семь"]], 38:[["тридцать восемь"]], 39:[["тридцать девять"]], 40:[["сорок"]], 41:[["сорок одна"]], 42:[["сорок две"]],
43:[["сорок три"]], 44:[["сорок четыре"]], 45:[["пятнадцати"]], 46:[["четырнадцати"]], 47:[["тринадцати"]], 48:[["двенадцати"]],
49:[["одиннадцати"]], 50:[["десяти"]], 51:[["девяти"]], 52:[["восьми"]], 53:[["семи"]], 54:[["шести"]],
55:[["пяти"]], 56:[["четырех"]], 57:[["трех"]], 58:[["двух"]], 59:[["одной"]]}  
          
time = input("Введите время в формате hh:mm: \n")
time = time.replace(" ", "").replace(".",":").replace(",",":")

check = '^([0-9]|([0,1][0-9])|(2[0-3])):[0-9]|[0-5][0-9]$'
if re.match(check, time) is None:
    print("Время указано не правильно")
    exit()

time = time.split(":") 

hh = int(time[0])
mm = int(time[1]) 

if hh > 12:
    hh = hh-12

hour = d[hh]
min = d[mm]

if mm == 0:
    if hh == 1:
        time_text = f"{hour[1][0]} час ровно"  
    elif hh >= 2 and hh <= 4:
        time_text = f"{hour[1][0]} часа ровно"  
    else:
        time_text = f"{hour[1][0]} часов ровно"  
elif mm < 30: 
    if mm == 1 or mm == 21:
        time_text = f"{min[0][0]} минута {hour[1][1]}"
    elif mm >= 2 and mm <=4 or mm >= 22 and mm <=24:
        time_text = f"{min[0][0]} минуты {hour[1][1]}"
    else:
        time_text = f"{min[0][0]} минут {hour[1][1]}"
elif mm == 30:
    time_text = f"половина {hour[1][1]}"
elif mm > 30 and mm < 45:
    if mm == 31 or mm == 41:
        time_text = f"{min[0][0]} минута {hour[1][1]}"
    elif mm >= 32 and mm <= 34 or mm >= 42 and mm <= 44:
        time_text = f"{min[0][0]} минуты {hour[1][1]}"
    else:
        time_text = f"{min[0][0]} минут {hour[1][1]}"
elif mm >= 45:
    if mm == 59:
        time_text = f"без {min[0][0]} минуты {hour[1][2]}"
    else:
        time_text = f"без {min[0][0]} минут {hour[1][2]}"
        
print(time_text)
