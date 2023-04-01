string_input = input('Enter a string that will remove all vowels:\n').upper()
letters = ['A', 'E', 'I', 'O', 'U', 'Y']

for i in string_input:
    if i in letters:
        string_input = string_input.replace(i, '')

print(f'String without vowels: {string_input}')
