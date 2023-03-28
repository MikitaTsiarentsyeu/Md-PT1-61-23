user_string = input("Enter the string: ").lower()

consonants = "bcdfghjklmnpqrstvwxyz"
count = 0

for letter in user_string:
    if letter in consonants:
        count += 1

print(f"The number of consonants in a line is {count}")