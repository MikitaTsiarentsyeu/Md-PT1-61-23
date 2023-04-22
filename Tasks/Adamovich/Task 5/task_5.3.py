#3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.

new_list = []

def look_for_strings (list):
    for i in list:
        if len(i) > 5:
            new_list.append (i)
    return new_list

print(look_for_strings (["spring is coming soon", "day"]))