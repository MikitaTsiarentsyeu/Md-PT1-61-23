#5.Write a program that generates a random number between in a given range, and shows the answer to a user.
from random import randint

range_min = int(input("MIN:"))
range_max = int(input("MAX:"))

print(randint(range_min, range_max))