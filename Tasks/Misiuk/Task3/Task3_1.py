input_string = input('Enter your string:\n').upper()

letters = ['A', 'E', 'I', 'O', 'U', 'Y']

print(f'Your string {input_string} has:\n')
for i in letters:
    print(f'Count {i} - {input_string.count(i)}')
