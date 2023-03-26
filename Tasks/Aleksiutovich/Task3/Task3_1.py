# Write a program that takes a string as input from a user and returns the number of vowels in the string.
# user_input = input("Enter your text: \n")
# user_input = "Test is test. the test a test"
count = 0
vowels = "aeiouy"
for x in input("Enter your text: \n> ").lower():
    if x in vowels:
        count += 1
print(f"The number of vowel letters in this string is {count}.")
