import itertools


def range_numbers(list_input: list) -> str:
    """
    Function for finding a range of numbers
    """
    str_o = ''
    for key, group in itertools.groupby(enumerate(list_input), lambda x: x[1] - x[0]):
        group = list(group)
        if len(group) == 1:
            str_o += str(group[-1][1]) + ', '
        else:
            str_o += str(group[0][1]) + '-'
            str_o += str(group[-1][1]) + ', '
    str_o = str_o.rstrip(', ')
    return str_o


list_input = [int(x)
              for x in input('Enter a number separated by a space: ').split() if x.isdigit()]

print(range_numbers(list_input))
