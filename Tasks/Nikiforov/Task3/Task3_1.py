# 1. Write a program that takes a string as input from a user and returns the number of vowels in the string.
UserString = input("Enter text: \n")
NumberOfVowels = 0 

Vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]

for i in UserString:
    if i in Vowels:
        NumberOfVowels += 1

print(f"The text contains {NumberOfVowels} vowels")