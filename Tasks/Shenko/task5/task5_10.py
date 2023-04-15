# Рекурсивная функция для поиска заданного числа в последовательности Фибоначчи
n = int(input("Введите номер элемента из последовательности Фибоначчи:\n"))

def fibonacci(n):
    if n in (1,2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))