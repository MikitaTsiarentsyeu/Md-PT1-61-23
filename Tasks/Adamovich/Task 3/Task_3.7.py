# Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.
string = input("Input your string in English: ")
print(type(string), string)

new_string = ""

for i in range(len(string)):
    if string[i].isupper():
        new_string += string[i].lower()
    elif string[i].islower():
        new_string += string[i].upper()
    else:
        new_string += string[i]

print(new_string)

