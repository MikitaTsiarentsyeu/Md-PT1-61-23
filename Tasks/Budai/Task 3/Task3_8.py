from input_numbers import input_list_of_numbers

numbers = input_list_of_numbers()

average = sum(numbers) / len(numbers)

print(f'Average of numbers in list is {average}')
