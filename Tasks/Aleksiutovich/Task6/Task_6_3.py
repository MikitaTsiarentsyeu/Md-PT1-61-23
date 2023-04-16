# -*- coding: utf-8 -*-
# Write a function that takes a list of integers as input and returns
# the sum of all even numbers in the list. Handle the TypeError and return
# "Invalid input type" if the input is not a list or not every element is int.

def sum_elems(val_list):
    try:
        return sum(val_list)
    except TypeError:
        return "Invalid input type"


# test
list_1 = ["a", 3, 4, 5, 6]
list1 = [1, 3, 4, 5, 6]
res = sum_elems(list_1)
print(res)
