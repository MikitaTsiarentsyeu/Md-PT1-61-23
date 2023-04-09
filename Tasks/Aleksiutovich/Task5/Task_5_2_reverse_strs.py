# -*- coding: utf-8 -*-
# Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.
list = ['test', 'test', 'test', 'test', 'test']
list1 = ['test', 'test', 'test', 'test', 'test', 1]
def reverse_strs(list):
    try:
        return [string[::-1] for string in list]
    except TypeError:
        print("Error. The list must consist of a string type")
#test
x = reverse_strs(list)
#x = reverse_strs(list1)
print(x)
