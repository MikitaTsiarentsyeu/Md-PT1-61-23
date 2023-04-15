# 2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.

def reversed_list(l:list) -> list:
    new_l = []
    for i in l:
        new_l.append(i[::-1])
    return new_l

user_string = input("enter strings separated by spaces:\n")
user_string = user_string.strip().split(' ')

print(reversed_list(user_string))

