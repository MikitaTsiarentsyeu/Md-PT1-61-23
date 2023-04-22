# -*- coding: utf-8 -*-
import random
# Write a function that takes two numbers as input and returns their division. Handle
# the ZeroDivisionError and return "Cannot divide by zero" if the denominator is zero.
def division(val1, val2):
    try:
        return val1 / val2
    except ZeroDivisionError:
        print("Cannot divide by zero")



# test
a = random.randint(0, 10)
b = random.randint(0, 3)
print(f"num1 = {a} and num2 = {b}")
res = division(a, b)
print(f" {a} / {b} = {res}")
