# -*- coding: utf-8 -*-
from Generetor_str import generate_random_string as test_str
# Write a recursive function to reverse a string.


def reverse_str(string):
    if len(string) == 0:
        return ''
    else:
        return string[len(string) - 1] + \
               reverse_str(string[:len(string) - 1])


# test
test = test_str(5)
print(test)
result = reverse_str(test)
print(result)
