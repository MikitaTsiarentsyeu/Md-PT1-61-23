# Write a program that takes a string as input and returns the string with all capital letters converted to lowercase
# and vice versa.
user_input = input("Enter your text: \n")
str_list = user_input.split()
for x in range(len(str_list)):
    for y in range(len(str_list[x])):
        if str_list[x][y].islower():
            str_list[x] = str_list[x].replace(str_list[x][y],
                                              str_list[x][y].upper())
        else:
            str_list[x] = str_list[x].replace(str_list[x][y],
                                              str_list[x][y].lower())
output_str = ' '.join(str_list)
print(output_str)
