# -*- coding: utf-8 -*-
from random import randint


# Write a recursive function to find the Nth number in the Fibonacci sequence.
# 0, 1, 2, 3, 5, 8, 13, 21, ...
# 1  2  3  4  5  6  7  8
def fibonacci_rec(Nth_number):
    if Nth_number <= 0:
        return 0
    elif Nth_number == 1:
        return 1
    else:
        return fibonacci_rec(Nth_number - 1) + fibonacci_rec(Nth_number - 2)


# test
a = randint(0, 30)
print(f'Nth number = {a}')
x = fibonacci_rec(a)
print(f'Result = {x}')
