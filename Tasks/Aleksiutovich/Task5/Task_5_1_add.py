# -*- coding: utf-8 -*-
from random import randint as random_int


# Write a function that takes two integers as arguments and returns their sum.
def add(num_1: int, num_2: int) -> int:
    if isinstance(num_1, int) and isinstance(num_2, int):
        return num_1 + num_2
    else:
        raise ValueError("Error. The numbers must be integers")


# test
for i in range(10):
    a = int(random_int(1, 99))
    b = int(random_int(1, 99))
    print(f'num1 = {a}, num2 = {b}')
    sum_nums = add(a, b)
    print(f'num1 + num2 = {sum_nums}')
