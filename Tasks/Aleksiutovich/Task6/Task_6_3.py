# -*- coding: utf-8 -*-
# Write a function that takes a list of integers as input and returns
# the sum of all even numbers in the list. Handle the TypeError and return
# "Invalid input type" if the input is not a list or not every element is int.

def sum_elems(val_list):
    try:
        if isinstance(val_list, __builtins__.list):
            return sum([x for x in val_list if x % 2 == 0])
        else:
            return "Invalid input type"
    except TypeError:
        return "Invalid input type"


# test
regular_list = [1, 2, 3, 4, 5]
# print(isinstance(regular_list, list))
list_1 = ["a", 3, 4, 5, 6]
not_list = 1, 3, 4, 5, 6
# res = sum_elems(list_1)
res = sum_elems(not_list)

print(res)
