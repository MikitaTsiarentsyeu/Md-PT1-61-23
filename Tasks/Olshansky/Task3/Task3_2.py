# Subtask 3_2
# 2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

users_input = [1, 2, 3, 4, 5, 0, 10, 125, 2.0]

sm = 0
for i in users_input:
    if i % 2 == 0:
        sm += i
print(sm)