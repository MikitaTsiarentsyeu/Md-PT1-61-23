# 8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.

def numbers(a):
    return (sum(a) / len(a)).__round__(3)


print(numbers(list(map(float, input().split()))))


