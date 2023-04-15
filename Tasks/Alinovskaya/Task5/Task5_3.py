
# 3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.
list_for_generate = ['Windows', 'macOS', 'Linux', '']

def generate_new_list (list_of_string):
    new_list = []
    for i in list_of_string:
        if len(i) > 5 :
            new_list.append(i);
    return new_list
print(generate_new_list(list_for_generate))