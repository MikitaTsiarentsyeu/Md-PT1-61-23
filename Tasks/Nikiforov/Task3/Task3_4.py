# 4. Write a program that takes a list of numbers as input and returns the second largest number in the list.
import re
numbs = input("Enter numbers separated by space:\n")
numbs = re.sub(' +', ' ', numbs)
numbs = numbs.strip().split(" ")
numbs = list(map(int, numbs))

maxn = max(numbs)

while maxn in numbs:
    numbs.remove(maxn)

print(f"The second largest number in the list:\n------------{max(numbs)}------------")
