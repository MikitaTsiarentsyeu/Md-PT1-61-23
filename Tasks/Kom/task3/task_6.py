s = input("Введите текст на русском языке:\n")
vowels = ["а", "о", "у", "ы", "э", "и", "е", "ё", "ю", "я"]

str = ""
for i in s:
    if i.isalpha():
        if i not in vowels:
            str += i
print(str)