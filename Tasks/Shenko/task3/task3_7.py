# заменить регистр

s = input("Введите текст в разном регистре:\n")

str = ""
for i in s:
    if i.islower():
        str += i.upper()
    else:
        str += i.lower()
print(str)