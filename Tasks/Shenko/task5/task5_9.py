# Рекурсивная функция для вычмсления степени заданного числа
a = int(input("Введите число:\n"))
b = int(input("Введите в какую степень Вы хотите возвести число:\n"))

def power(a,b):
    if b == 1:
        return a
    return a * power(a, b-1)
print(power(a,b))