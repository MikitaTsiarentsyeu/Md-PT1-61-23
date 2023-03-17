Celsius = int(input("Введите, пожалуйста, градусы Цельсии ... "))
Fahrenheit = (Celsius * 1.8) + 32
Fahrenheit = round(Fahrenheit)
print("Будет " + str(Fahrenheit) + " градусов по Фаренгейту")

import math
radius = int(input("Введите, пожалуйста, радиус окружности ... "))
area_of_a_circle = math.pi * (radius*radius)
print("Площадь круга равна " + str(area_of_a_circle))

kilometers_per_hour = int(input("Введите, пожалуста, скорость в километрах в час ... "))
meters_per_second = round((kilometers_per_hour * 1000) // 3600)
print("Скорость равна " + str(meters_per_second) + " метров в секунду")


amound_USD = int(input("Укажите, пожалуйста, сумму (в USD) ... "))
ratio = float(input("Укажите, пожалуйста, курс, по кторому будет осуществляться перевод ... "))
amound_BYN = amound_USD * ratio
amound_BYN = round(amound_BYN, 2)
print(f"курс: {ratio} сумма BYN: {amound_BYN}")

import random 
first_range = int(input("Задайте, пожалуйста, диапазон (начало диапазона ... )"))
end_range = int(input("Задайте, пожалуйста, диапазон (конец диапазона ... )"))
random_number = random.randint(first_range, end_range)
print(f"случайное число: {random_number}")



