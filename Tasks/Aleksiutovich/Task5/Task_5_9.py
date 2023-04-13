# -*- coding: utf-8 -*-
from random import randint


# Write a recursive function to calculate the power of a given number.
def power(num, exponent):
    if exponent == 0:
        return 1
    elif num == 0:
        # иначе будет выводить 1
        return 0
    else:
        return num * power(num, exponent - 1)


# test
# x = power(2,4)
# x1 = power(1,3)
# x2 = power(0,5)
#
# print(x)
# print(x1)
# print(x2)
a, b = randint(0, 20), randint(0, 9)
print(f'num = {a} and exponent = {b}')
x = power(a, b)
print(f'Result = {x}')
