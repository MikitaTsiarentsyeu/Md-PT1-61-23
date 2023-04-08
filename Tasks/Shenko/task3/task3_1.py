# вернуть строку без гласных

s = input("Введите текст на русском языке:\n")
vowels = ["а", "о", "у", "ы", "э", "и", "е", "ё", "ю", "я"]

count = 0
for i in s.lower():
    if i.isalpha():
        if i in vowels:
            count += 1
            print(f"гласная {i}")
print(f"Во введенной Вами строке {count} гласных.\n")