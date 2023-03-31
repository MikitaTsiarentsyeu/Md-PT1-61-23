# 8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
from statistics import mean;
list_num = [1, 3, 56, 78, 4, 8, 10, 12, 46, 29, 400, 300, 219, 501, 101, 42, 15, 64];
average = mean(list_num);
print(f"the average of all numbers in the list is {average}");
