def len_str_of_list(list:list) ->list:
    """
    This function returns a list with lines longer than 5.
    """
    list_out = [x for x in list if len(x) > 5]
    return list_out

list_str = input('Enter your string:\n').split()
print(f'List of strings longer than 5: {len_str_of_list(list_str)}')