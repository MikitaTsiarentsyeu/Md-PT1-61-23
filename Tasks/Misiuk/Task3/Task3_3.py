input_string = input('Enter your string: ').lower().replace(
    ',', ' ').replace('.', ' ').split()

str_dict = {}
for word in input_string:
    if word in str_dict:
        str_dict[word] += 1
    else:
        str_dict[word] = 1

print(str_dict)
