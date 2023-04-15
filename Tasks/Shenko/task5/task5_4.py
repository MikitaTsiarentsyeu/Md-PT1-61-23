# возвращает кол-во символов нижнего и верхнего регистров в исходной строке

str = input("Введите строку с буквами в верхнем и нижнем регистре:\n")

def register(str):
    count_up = 0
    count_lo = 0
    for i in str:
        if i.isupper():
            count_up += 1
        if i.islower():
            count_lo += 1
    return (f"Количечтво букв в верхнем регистре: {count_up}\nКоличество букв в нижнем регистре: {count_lo}")
print(register(str))