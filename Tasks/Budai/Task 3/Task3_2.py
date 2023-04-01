from input_numbers import input_list_of_numbers

numbers = input_list_of_numbers()
sum_of_even = 0

for n in numbers:
    if n % 2 == 0:
        sum_of_even += n

print(f'Sum of even numbers is {sum_of_even}')
