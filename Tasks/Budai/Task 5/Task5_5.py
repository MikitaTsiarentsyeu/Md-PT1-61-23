def get_ranges_for_numbers_in_list(numbers):
    res = ''
    begin = end = numbers[0]
    for n in numbers[1:]:
        if n == end + 1:
            end = n
        else:
            if begin != end:
                res += f'{begin}-{end}, '
            else:
                res += f'{begin}, '
            begin = end = n
    if begin != end:
        res += f'{begin}-{end}.'
    else:
        res += f'{begin}.'
    return res


numbers = [int(n) for n in input('Input numbers separated with space: ').split()]
print(get_ranges_for_numbers_in_list(numbers))
