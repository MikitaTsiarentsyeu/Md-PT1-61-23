# -*- coding: utf-8 -*-
from random import randint as random_int


# Write a function that takes two integers as arguments and returns their sum.
def add(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError("Error. The numbers must be integers")


# good test
for i in range(10):
    a = int(random_int(1, 99))
    b = int(random_int(1, 99))
    print(f'num1 = {a}, num2 = {b}')
    sum_nums = add(a, b)
    print(f'num1 + num2 = {sum_nums}')
    # bad test
    add(2.4, 4)
