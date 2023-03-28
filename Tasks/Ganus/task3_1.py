str_enter = input("Введите, пожалуйста, строку для подсчёта гласных\n")
str_enter = str_enter.lower()
count = 0
for letter in str_enter:
    if letter == "у" or letter == "е" or letter == "ы" or letter == "а" or letter == "о" or letter == "э" or letter == "я" or letter == "и" or letter == "ю" or letter == "ё":
        count = count + 1
print(f"В строке \"{str_enter}\" - {count} гласных")

