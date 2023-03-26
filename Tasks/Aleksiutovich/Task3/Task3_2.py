# Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.
input_user = input("Enter numbers seperated by a space \n > ")
input_user = [int(numbers) for numbers in input_user.split()]
sum_even_nums = 0
for num in input_user:
    if num % 2 == 0:
        sum_even_nums += num
print(f"The sum of all even numbers in the list is {sum_even_nums}")
