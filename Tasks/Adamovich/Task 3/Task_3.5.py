# Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.

entered_list = input("Enter a list of strings by spaces: ").split()
print(entered_list)

max_len = 5
new_list = []
for element in entered_list:
    if len(element) > max_len:
        new_list.append(element)
print(f"Strings that have a length greater than 5 characters are {new_list}")

