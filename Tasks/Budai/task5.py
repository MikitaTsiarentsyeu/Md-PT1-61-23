import random

min_border = int(input('Enter minimal border: '))
max_border = int(input('Enter maximal border: '))
random_number = random.randint(min_border, max_border)

print(f'Random number from the range is {random_number}')
