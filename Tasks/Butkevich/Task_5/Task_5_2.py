# 2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all
# reversed.

def revers(a):
    l = []
    for i in a:
        l.append(i[::-1])

    return l[::-1]


print(revers(list(map(str, input().split()))))
