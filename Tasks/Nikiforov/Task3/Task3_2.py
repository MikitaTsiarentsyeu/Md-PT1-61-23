# 2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.
import re
numbs = input("Enter numbers separated by space:\n")
numbs = re.sub(' +', ' ', numbs)
numbs = numbs.strip().split(" ")
numbs = list(map(int, numbs))

sum = 0
for i in range(len(numbs)):
    if numbs[i] % 2 == 0:
        sum += numbs[i]
print(f"The sum of all even numbers: {sum}")

