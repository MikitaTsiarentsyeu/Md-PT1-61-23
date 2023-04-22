# 3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have
# a length greater than 5

def revers(a):
    l = []
    for i in a:
        if len(i) > 5:
            l.append(i)

    return l


print(revers(list(map(str, input().split()))))
