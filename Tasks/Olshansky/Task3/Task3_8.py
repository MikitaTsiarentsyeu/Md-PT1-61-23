# Subtask 3_8
# 8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9.76, -10]
av = 0
sum = 0
for n in l:
    sum = sum + n
av = sum / len(l)
print(av)
