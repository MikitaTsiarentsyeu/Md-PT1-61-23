# Write a program that takes a list of numbers as input and returns the second largest number in the list.
input_user = input("Enter numbers seperated by a space \n > ")
input_user = [int(numbers) for numbers in input_user.split()]
print("Converted a string to a list")
print(input_user)
if len(input_user) == 1:
    print("Error. Need more than one value")
else:
    input_user.sort()
    print("The second largest number is " + str(input_user[-2]) + " in the list")
