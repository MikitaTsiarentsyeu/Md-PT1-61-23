# Subtask 3_4
# 4. Write a program that takes a list of numbers as input and returns the second largest number in the list.

users_input = [15, 10, 13, 2, 5, 8, 9, 0, 13.5,123]
users_input.sort()
# print(users_input)

count = -1
for i in range(len(users_input)):
    if users_input[count] != users_input[(count) - (i)]:
        print(users_input[(count) - (i)])
        break