# -*- coding: utf-8 -*-
from Generetor_str import generate_random_string as test_str
# Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.
def reverse_strs(list):
    try:
        return [string[::-1] for string in list]
    except TypeError:
        print("Error. The list must consist of a string type")
#test
test = [test_str(5) for x in range(5)]
print(test)
result = reverse_strs(test)
print(result)
