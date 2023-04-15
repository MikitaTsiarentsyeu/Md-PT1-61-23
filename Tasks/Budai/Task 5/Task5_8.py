def number_of_occurrences(string, char):
    if string == '':
        return 0
    elif char == string[0]:
        return 1 + number_of_occurrences(string[1:], char)
    else:
        return number_of_occurrences(string[1:], char)


string = input('Input string: ')
char = input('Input character: ')

print(f'Number of occurrences is {number_of_occurrences(string, char)}')
