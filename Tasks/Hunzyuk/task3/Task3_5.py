list_names = list(map(str, input("Enter words separated by spaces: ").split()))

new_list_names = []

for elem in list_names:
    if len(elem) > 5:
        new_list_names.append(elem)

print(new_list_names)