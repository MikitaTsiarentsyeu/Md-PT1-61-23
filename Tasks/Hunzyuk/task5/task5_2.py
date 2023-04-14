lst_string = [str(i) for i in input("Enter lines separated by spaces: ").split()]

def revers_list_strings(lst_string):
    result_list = []
    for string in lst_string:
        result_list.append(string[::-1])
    return result_list

print(revers_list_strings(lst_string))