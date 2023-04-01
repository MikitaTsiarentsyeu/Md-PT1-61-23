# 5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.
def string(a):
    l = []
    for i in a:
        if len(i) > 5:
            l.append(i)
    return l


print(string(list(input().lower().split())))
