list_input = input('Enter the number: ').split(',')

liset = set(list_input)
list_output = []
for i in liset:
    if i.isdigit:
        list_output.append(int(i))
list_output.sort(), list_input.sort()

print(
    f'Second largest number on the list: {list_input}\nis the number: {list_output[1]}')
