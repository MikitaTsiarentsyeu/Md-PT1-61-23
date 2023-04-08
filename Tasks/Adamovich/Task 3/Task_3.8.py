# Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
entered_list = input("Enter a list of numbers separated by spaces: ").split()
converted_entered_list = [int(i) for i in entered_list]
print(f"Entered list of numbers: {converted_entered_list}", type(converted_entered_list))

#option 1
from statistics import mean
average = mean(converted_entered_list)
print(f"average of all numbers in the list is {average}")

#option 2
average = int(sum(converted_entered_list) / len(converted_entered_list))
print(f"average of all numbers in the list is {average}")
