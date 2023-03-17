import math
import decimal
import random


# Task 1.1

celsius = int(input("Введите температуру в градусах Цельсия: "))
frht = int(celsius*1.8+32)
print("Температура равна", frht, "градусам по Фаренгейту")


# Task 1.2

rad = int(input("Введите значение радиуса: "))
sqrt = round((math.pi*rad**2), 2)
print("Площадь круга составляет", sqrt)


# Task 1.3

km_p_h = int(input("Введите скорость в км/ч: "))
print("Скорость", km_p_h, "км/ч равна", int(km_p_h*1000/3600), "м/с")


# Task 1.4

ex_rate = decimal.Decimal('2.83')
am_usd = int(input("Сумма в долларах США: "))
am_byn = ex_rate*am_usd
print(am_usd, "$ ==>", am_byn, "руб.")


# Task 1.5

bottom_border = int(input("Введите нижнюю границу диапазона: "))
upper_border = int(input("Введите верхнюю границу диапазона: "))
print("Результат ---------------> ", random.randint(bottom_border, upper_border))
