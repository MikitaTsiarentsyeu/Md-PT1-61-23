# -*- coding: utf-8 -*-
from Generetor_str import generate_random_string as test_str
# Write a function that takes a list of strings as an argument and returns
# a new list with all the strings that have a length greater than 5.
def len_strs(list):
    try:
        return [string for string in list if len(string) > 5]
    except TypeError:
        print("Error. The list must consist of a string type")
#test
test = [test_str(x) if x%2==0 else test_str(x*2) for x in range(3,10)]
print(test)
result = len_strs(test)
print(result)