# -*- coding: utf-8 -*-
from Generetor_str import generate_random_string as test_str
# Write a function that takes a string as an argument and returns two numbers, first for count of lower case symbols,
# second for count of the upper case symbols in the initial string.

def count_case(str):
    lower_case = sum((1 for letter in str if letter.islower()))
    upper_case = sum((1 for word in str if word.isupper()))
    return lower_case, upper_case


# test
test = test_str(8)
print(test)
result = count_case(test)
print(result)





