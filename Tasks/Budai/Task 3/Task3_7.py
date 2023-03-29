string = input('Input string: ')
result_string = ''

for c in string:
    if c.islower():
        result_string = result_string + c.upper()
    else:
        result_string = result_string + c.lower()

print(f'String with swapped case - {result_string}')

# string.swapcase()
