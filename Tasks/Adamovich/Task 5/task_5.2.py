#2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.

new_list = []

def reversed_strings (list):
    for i in list:
        i = i[::-1]
        new_list.append (i)
    return new_list

print(reversed_strings (["spring", "summer"]))