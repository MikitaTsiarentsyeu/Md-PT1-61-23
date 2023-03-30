# 10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.


def numbers(a):
    lst = []
    for i in a:
        l = []
        for j in a:
            if i % j == 0:
                l.append(j)
        if len(l) == 2:
            lst.append(i)

    return max(lst)


print(numbers(list(map(int, input().split()))))
