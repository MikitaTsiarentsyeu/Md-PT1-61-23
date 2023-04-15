#  вернет слова в обратном порядке (не меняя буквы в самих словах)
def reverse(str):
    return str[::-1]
l = input("Введите несколько слов:\n")
str = l.split()
print(reverse(str))


# переставит местами и слова и буквы в словах
def reverse(l):
    return l[::-1]
l = input("Введите несколько слов:\n")
print(reverse(l))
