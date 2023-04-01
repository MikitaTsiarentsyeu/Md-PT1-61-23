from math import sqrt

list_numbers = list(map(int, input("Enter whole numbers: ").split()))
number = 0

new_lst = []

for item in list_numbers:
    i = 2
    while i <= sqrt(item):
        if item % i == 0:
            break
        i += 1
    else:
        if item not in (0, 1):
            new_lst.append(item)

print(max(new_lst))