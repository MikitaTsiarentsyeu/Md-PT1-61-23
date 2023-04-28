# -*- coding: utf-8 -*-
import random
import pickle
from functools import lru_cache

# Write a decorator function that caches the return value of
# a function with a dictionary.
# If the function is called again with the same arguments,
# return the cached value instead of computing it again.

cache = {}


def cache_decorator(func):
    global cache
    #cache = {}
    def wrapper(*args, **kwargs):
        key = pickle.dumps(args) + pickle.dumps(args)
        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper


# test
# Функция add принимает два аргумента и возвращает их сумму:
@cache_decorator
def add(x, y):
    return x + y
# Функция multiply принимает два аргумента и возвращает их произведение:
@cache_decorator
def multiply(x, y):
    return x * y
# Функция reverse_string принимает строку в качестве аргумента и возвращает ее в обратном порядке:
@cache_decorator
def reverse_string(s):
    return s[::-1]
# Функция is_even принимает число в качестве аргумента и возвращает True, если число четное, и False в противном случае:
@cache_decorator
def is_even(n):
    return n % 2 == 0
# Функция get_first_element принимает список в качестве аргумента и возвращает его первый элемент:
@cache_decorator
def get_first_element(lst):
    return lst[0]

multiply(2,4)
for count in range(10):
    a = random.randint(1, 2)
    b = random.randint(1, 2)
    add(a, b)
test = add(2, 2)
get_first_element([1, 2, 3])
get_first_element([1, 2, 3])
is_even(4)
is_even(5)
reverse_string('asdfdsf')
reverse_string('[1,2,3]')
print(cache)
