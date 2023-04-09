# -*- coding: utf-8 -*-
import random
# Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
def get_ranges(list):
    ranges = []  # список для хранения диапазонов
    start = end = list[0]  # начальные значения диапазона
    for num in list[1:]:  # перебираем все числа списка начиная со второго
        if num == end + 1:  # если число следующее за текущим, то это продолжение диапазона
            end = num  # обновляем конец диапазона
        else:  # если число не следующее за текущим, то это начало нового диапазона
            ranges.append(f"{start}-{end}" if start != end else f"{start}")  # добавляем предыдущий диапазон в список
            start = end = num  # обновляем начало и конец нового диапазона
    ranges.append(f"{start}-{end}" if start != end else f"{start}")  # добавляем последний диапазон в список
    return ", ".join(ranges)  # возвращаем список диапазонов в виде строки, разделенной запятыми


# test
def random_generator():
    list1 = [0, 1, 2, 3, 4, 7, 8, 10]
    while True:
        yield random.choice(list1)


# print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
# print(get_ranges([4, 7, 10]))
# print(get_ranges([2, 3, 8, 9]))
test = [next(random_generator()) if x % 4 == 0 else x for x in range(random.randint(4, 20))]
print(test)
print(get_ranges(test))
