def reverse_string(s):
    return ''.join(reversed(s))


def get_list_with_reversed_strings(*args):
    res = []
    for s in args:
        s = reverse_string(s)
        res.append(s)
    return res


strings = [s for s in input('Input strings separated with space: ').split()]

print(get_list_with_reversed_strings(*strings))
