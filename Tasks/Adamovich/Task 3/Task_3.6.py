# Write a program that takes a string as input and returns the string with all vowels removed.
# option №1
string = input("Input your string in English: ")
print(type(string), string)

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
result = ""

for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]

print (f"String with all vowels removed is {result}")

# option №2
for i in vowels:
    string = string.replace (i, '')

print (f"String with all vowels removed is {string}")

