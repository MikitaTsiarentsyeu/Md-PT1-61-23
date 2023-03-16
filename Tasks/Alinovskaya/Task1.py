
# import math;
# import decimal;
# import random;
from datetime import datetime;
import datetime as DT;


# # 1 
# degrees_celcia = 4;
# degrees_fahrenheit = degrees_celcia * 1,8 + 32;
# print('converts Celsius to Fahrenheit', degrees_fahrenheit);

# #2
# num_radius = 52;
# area_of_circle = round(math.pi * num_radius**2);
# print('area of circle equal', area_of_circle);

# #3
# km_pr_hr = 120;
# mt_pr_sc = round(km_pr_hr * (1000/3600));
# print(mt_pr_sc, 'meters per second');

# #4
# sum_money_USA = 100;
# exchange_rates = 2.85;
# sum_money_BLR = decimal.Decimal(sum_money_USA * exchange_rates);
# print('money exchange - ', sum_money_BLR, 'blr');

# #5
# a = -888;
# b = 888;
# random_number = random.randint(a, b);
# print(random_number, 'it is a random number between in a given range');


#6
user = input("Enter your birthday in format: yyyy.mm.dd");

first_date = DT.datetime.strptime(user, '%Y.%m.%d').date();

current_date = datetime.now();
second_date= current_date.date();

delta = second_date - first_date;

year = delta / 365;

print(year.days);


