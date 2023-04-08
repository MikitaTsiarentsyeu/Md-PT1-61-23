# 8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
import re
numbs = input("Enter numbers separated by space:\n")
numbs = re.sub(' +', ' ', numbs)
numbs = numbs.strip().split(" ")
numbs = list(map(float, numbs))
sum = 0 

for i in numbs:
    sum += i

avg = sum/len(numbs)

print(f"The average of all numbers: {avg}")