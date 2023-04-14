# рекурсивная функция для обращения строки
s = str(input("Введите строку:\n"))

def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]
print(s)
print(reverse(s))