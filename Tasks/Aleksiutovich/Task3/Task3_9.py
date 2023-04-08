# Write a program that takes a string as input and returns the string reversed.
input_user = input("Enter your text \n />")
#input_user = "Enter is name"
output_str = ''
for x in range(len(input_user) - 1, -1, -1):
    output_str += output_str.join(input_user[x])
print(output_str)
