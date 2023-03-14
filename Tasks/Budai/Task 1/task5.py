import random

min_border = int(input('Enter minimal border: '))
max_border = int(input('Enter maximal border: '))

if min_border == max_border or min_border > max_border:
    print('Invalid input! Maximal border should be more than minimal')
else:
    random_number = random.randint(min_border, max_border)
    print(f'Random number from the range is {random_number}')
