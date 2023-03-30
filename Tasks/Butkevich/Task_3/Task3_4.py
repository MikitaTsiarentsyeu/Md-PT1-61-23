# 4. Write a program that takes a list of numbers as input and returns the second largest number in the list.

def numbers(a):
    l = []
    for i in a:
        l.append(i)
    l.remove(max(l))
    return max(l)


print(numbers(list(map(int, input().split()))))
