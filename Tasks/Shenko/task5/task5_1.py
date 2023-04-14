# написать функцию, которая принимает в качестве аргументов два целых числа и возвращает их сумму
while True:
    a = input("Введите первое число:\n")
    b = input("Введите второе число:\n")
    if not a.isdigit() and not b.isdigit():
        print("Вводите целые числа!\n")
        continue
    a = int(a)
    b = int(b)
    break

def sum(a,b):
    return a+b

print(f"Сумма введенных чисел равна: {sum(a,b)}")