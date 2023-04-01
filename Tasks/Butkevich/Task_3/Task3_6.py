# 6. Write a program that takes a string as input and returns the string with all vowels removed.

def script(a):
    l = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы", "a", "e", "i", "o", "u", "y"]
    for i in a:
        if i in l:
            a.replace(i," ",1)
    return a


print(script(input().lower()))
