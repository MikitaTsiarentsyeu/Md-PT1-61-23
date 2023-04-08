# Write a program that takes a string as input and returns a dictionary with the count of each word in the string.
string = input("Input your string: ")
print(string)

d = {}

for symbol in string:
    if symbol in d:
        d[symbol] += 1
    else:
        d[symbol] = 1

print(d)

