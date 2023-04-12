def reverse_string(s):
    if s == '':
        return s
    else:
        return reverse_string(s[1:]) + s[0]


string = input('Input string: ')

print(f'Reversed string: {reverse_string(string)}')
