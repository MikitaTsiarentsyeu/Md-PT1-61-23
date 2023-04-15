list_numbers = [1, 2, 3, 4, 7, 8, 10]

def get_ranges(list_numbers):
    string = ''
    start = end = list_numbers[0]
    
    for i in list_numbers[1:]:
        if i == end + 1:
            end = i
        else:
            if start != end:
                string += f'{start}-{end}, '
            else:
                string += f'{start}, '
            start = end = i
    
    if start == end:
        string += f'{start}'
    else:
        string += f'{start}-{end}'
    
    return string

print(get_ranges(list_numbers))