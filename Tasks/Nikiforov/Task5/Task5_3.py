#3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.

def list_greater_five(l:list) -> list:
    new_l = []
    for i in l:
        if len(i)>5:
            new_l.append(i)
    return new_l

user_list = input("enter strings separated by spaces:\n")
user_list = user_list.split(' ')

print(list_greater_five(user_list))
