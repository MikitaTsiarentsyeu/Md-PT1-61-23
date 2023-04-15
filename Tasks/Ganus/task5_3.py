def list_strings_revers(a: list) -> list:
    new_list = []
    for i in a:
        i = str(i)
        if len(i) > 5:
            new_list.append(i)
    return new_list
a = ["kill", "kitten", "home", "cat", "monday", "seven"]        
print(list_strings_revers(a))