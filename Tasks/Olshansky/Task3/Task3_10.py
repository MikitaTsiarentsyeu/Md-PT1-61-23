# Subtask 3_10
# 10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9.76, -10]
num_list = []
for i in l:
    count = 0
    i = int(i)
    if (i == 2) or (i % 2 != 0) and (i != 1) and (i != 0):
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count > 1:
            continue
        else:
            num_list.append(i)
print(max(num_list))