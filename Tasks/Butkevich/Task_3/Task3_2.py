# 2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

def summa(a):
    l = []
    for i in a:
        if i % 2 == 0:
            l.append(i)

    return sum(l)


print(summa(map(int, input().split())))
