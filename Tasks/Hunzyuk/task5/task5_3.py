lst_string = [str(i) for i in input("Enter lines separated by spaces: ").split()]

def list_long_strings(lst_string):
    result_list = []

    for string in lst_string:
        if len(string) > 5:
            result_list.append(string)
    return result_list

print(list_long_strings(lst_string))
