user_string = input("Enter the string: ").lower()

vowels = "aeiou"
count = 0

for letter in user_string:
    if letter in vowels:
        count += 1

print(f"The number of consonants in a line is {count}")