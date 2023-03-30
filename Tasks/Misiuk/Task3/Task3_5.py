list_input = input('Enter your string:\n')
list_output = []
signs = [',', '.', '!', '?', ':', ';', '"',
         "'", '#', '%', '@', '$', '^', '*', '<', '>']

for i in signs:
    list_input = list_input.replace(i, ' ')

for word in list_input.split():
    if len(word) > 5:
        list_output.append(word)
print(f'List of words longer than 5:\n{list_output}')
