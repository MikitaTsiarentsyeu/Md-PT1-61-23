# 1. Write a program that takes a string as input from a user and returns the number of vowels in the string.


def script(a):
    l = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы", "a", "e", "i", "o", "u", "y"]
    count = 0
    for i in a:
        if i in l:
            count += 1
    return count


print(script(input().lower()))
