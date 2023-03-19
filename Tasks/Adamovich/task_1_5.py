#5 Write a program that generates a random number between in a given range, and shows the answer to a user.
import random
range_low = int(input("Input the lower limit of the interval as integer: "))
range_upper = int(input("Input the upper limit of the interval as integer: "))
print(random.randint(range_low, range_upper))