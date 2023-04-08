# Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

entered_list = input("Enter a list of numbers separated by spaces: ").split()
converted_entered_list = [int(i) for i in entered_list]
print(f"Entered list of numbers: {converted_entered_list}")


sum_even = 0
for i in converted_entered_list:
      if i % 2 == 0:
          sum_even += i
print(f"Sum of all even numbers is {sum_even}")
