from input_numbers import input_list_of_numbers
from math import sqrt

numbers = input_list_of_numbers()
largest_prime = -1

for n in numbers:
    count = 0
    for div in range(2, int(sqrt(n)) + 1):
        if n % div == 0:
            count += 1
    if count == 0 and n > largest_prime:
        largest_prime = n

if largest_prime == -1:
    print('There are no prime numbers in the list.')
else:
    print(f'Largest prime number is {largest_prime}')
