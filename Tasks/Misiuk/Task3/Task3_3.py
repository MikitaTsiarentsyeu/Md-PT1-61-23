input_string = input('Enter your string: ').lower()
str_dict = {}

signs = [',', '.', '!', '?', ':', ';', '"',
         "'", '#', '%', '@', '$', '^', '*', '<', '>']


for i in signs:
    input_string = input_string.replace(i, ' ')
for word in input_string.split():
    if word in str_dict:
        str_dict[word] += 1
    else:
        str_dict[word] = 1

print(str_dict)
