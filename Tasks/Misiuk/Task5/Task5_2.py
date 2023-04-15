def reversed_list_string(lis:list) -> list:
    """
    Reverse list of string
    """
    list_out = [x[::-1] for x in lis]
    return list_out

list_str = input('Enter your string:\n').split()
print(f'Original list: {list_str}')
print(f'Reversed list: {reversed_list_string(list_str)}')