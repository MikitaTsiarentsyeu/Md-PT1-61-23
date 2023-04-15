# -*- coding: utf-8 -*-
# Write a recursive function to check whether a given string is a palindrome.
def check_palindrome(str):
    if len(str) == 0:
        return ''
    return str[-1] + check_palindrome(str[:-1])

def is_palindrome(str):
    return str == check_palindrome(str)


#test
print(is_palindrome('racecar')) # True
print(is_palindrome('hello')) # False