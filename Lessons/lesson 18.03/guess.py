import random

my_number = random.randint(0, 10)

your_number = int(input("Guess my number (from 0 to 10):\n"))

if my_number == your_number:
    print("Correct!")
else:
    print("Looooser!")
    print("My number was", my_number)