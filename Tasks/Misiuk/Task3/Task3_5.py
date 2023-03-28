list_input = input('Enter your string:\n').replace(',', ' ').split()
list_output = []
for word in list_input:
    if len(word) > 5:
        list_output.append(word)
print(f'List of words longer than 5:\n{list_output}')
