# Write a program that takes a string as input and returns a dictionary with the count of each word in the string.
input_user = input("Enter your text \n />")
input_user = input_user.upper()
marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
for world in input_user:
    if world not in marks:
        continue
    input_user = input_user.replace(world, " ")
input_user = input_user.split()
count = {}
for x in input_user:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
print(count)
