# Write a program that takes a string as input and returns the string with all vowels removed.
# user_input = input("Enter your text: \n")
user_input = "Test is test. the test a test"
vowels = "aeiouy"
new_str = ""
for x in user_input:
    if x in vowels:
        continue
    else:
        new_str += x
print(new_str)
