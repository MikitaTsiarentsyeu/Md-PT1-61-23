# Write a program that takes a list of numbers as input and returns the second largest number in the list.
entered_list = input("Enter a list of numbers separated by spaces: ").split()
converted_entered_list = [int(i) for i in entered_list]
print(f"Entered list of numbers: {converted_entered_list}")
print(sorted(converted_entered_list))
print(f"the second largest number in the list is {sorted(converted_entered_list)[-2]}")