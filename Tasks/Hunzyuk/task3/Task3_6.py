user_string = input("Enter text: ").lower()

vowels = "aeouyi"
result_string = ''

for letter in user_string:
    if letter not in vowels:
        result_string += letter
        
print(f"result is {result_string}")