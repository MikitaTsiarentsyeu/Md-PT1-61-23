# Write a program that takes a list of numbers as input and returns the largest prime number in the list.
entered_list = input("Enter a list of numbers separated by spaces: ").split()
converted_entered_list = [int(i) for i in entered_list]
print(f"Entered list of numbers: {converted_entered_list}", type(converted_entered_list))

prime_numbers_list = []

for num in converted_entered_list: 
 if num > 1: 
   for i in range(2,num): 
     if (num % i) == 0: 
       break 
   else:
     prime_numbers_list.append(num)
print(prime_numbers_list)
print(f"the largest prime number in the list is {max(prime_numbers_list)}") 