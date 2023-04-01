# 3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string.

def my_dic(a):
    d = {}
    for i in a:
        key, value = i, a.count(i)
        if a.count(i) == i:
            value += 1
            key, value = i, value
        d.update({key: value})
    return d


print(my_dic(input().split()))
