# Write a program that takes a string as input and returns the string reversed.

#option 1
string = input("Input your string in English: ")
print(type(string), string)
print(f"reversed string is {string[::-1]}")

#option 2
print(f"reversed string is {''.join(reversed(string))}")

