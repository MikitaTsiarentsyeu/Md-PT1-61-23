# 2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.
list_num = [1, 3, 56, 78, 4, 8, 10, 12, 46, 29, 400, 300, 219, 501, 101, 42, 15, 64];
result_sum = 0;

for num in list_num:
    if num % 2 == 0:
        result_sum += num;

print(f"the sum of all even numbers is {result_sum}")
