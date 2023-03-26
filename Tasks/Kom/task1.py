import math
import random 

#1
Cel = int(input("Введите градусы Цельсия ... "))
Far = (Cel * 1.8) + 32
Far = round(Far)
print("Будет " + str(Far) + " градусов по Фаренгейту")

#2
radius = int(input("Введите радиус круга ... "))
area = math.pi * (radius*radius)
print("Площадь круга равна " + str(area))

#3
km_h = int(input("Введите скорость в километрах в час ... "))
m_s = round((km_h * 1000) // 3600)
print("Скорость равна " + str(m_s) + " метров в секунду")

#4
amound_USD = int(input("Введите сумму в USD ... "))
ratio = float(input("Укажите курс, по которому осуществится перевод ... "))
amound_BYN = amound_USD * ratio
amound_BYN = round(amound_BYN, 2)
print(f"курс: {ratio} сумма BYN: {amound_BYN}")

#5
first_range = int(input("Укажите начало диапазона:"))
end_range = int(input("кажите конец диапазона:"))
random_numb = random.randint(first_range, end_range)
print(f"случайное число: {random_numb}")