vowels = 'aeiouy'
string = input('Input string: ')

result_string = ''

for c in string:
    if c.lower() not in vowels:
        result_string = result_string + c

print(f'String without vowels - {result_string}')
