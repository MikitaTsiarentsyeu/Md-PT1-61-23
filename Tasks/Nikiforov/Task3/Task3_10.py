#10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.
import re
numbs = input("Enter numbers separated by space:\n")
numbs = re.sub(' +', ' ', numbs)
numbs = numbs.strip().split(" ")
numbs = list(map(int, numbs))

primes = []

for i in numbs:
    count = 0
    for j in range(2, i):
        if (i % j == 0):
            count += 1 
    if (count <= 0):
        primes.append(i)

print(f"The largest prime number is {max(primes)}")

