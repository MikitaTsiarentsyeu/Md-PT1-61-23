str_enter = input("Введите, пожалуйста, строку\n")
str_enter = str_enter.lower()
str_enter = str_enter.replace(',', '').replace('.', '').replace(':', '').replace('-', '').replace('!', '').replace('?', '')
str_enter = str_enter.split(" ")
letter_count = {letter: str_enter.count(letter) for letter in str_enter}
print(letter_count)
