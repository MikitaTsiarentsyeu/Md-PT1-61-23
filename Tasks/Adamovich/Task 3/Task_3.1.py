# Write a program that takes a string as input from a user and returns the number of vowels in the string.
string = input("Input your string in English: ")
print(string)
       
l_vowels = ['a', 'e', 'i', 'o', 'u','y','A', 'E', 'I', 'O', 'U','Y']
vowels = 0

for letter in string:
    if letter in l_vowels:
        vowels = vowels + 1
print(f"Amount of vowels is {vowels}")
