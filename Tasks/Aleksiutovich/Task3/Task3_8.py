# Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
input_user = input("Enter numbers seperated by a space \n > ")
input_user = [int(numbers) for numbers in input_user.split()]
print(f"the average of all numbers {sum(input_user) / len(input_user)}  in the list")
