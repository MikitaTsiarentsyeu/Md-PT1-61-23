# -*- coding: utf-8 -*-
# Write a recursive function to count the number of occurrences of a given character in a string.
def count_letter(string, letter, count=0):
    if len(string)==0:
        return count
    first_let = string[0]

    if first_let == letter:
        count +=1

    return count_letter(string[1:],letter,count)


x = count_letter('aabssaaa', 'a')
print(x)
