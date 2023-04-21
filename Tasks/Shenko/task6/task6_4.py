
# Напишите функцию-декоратор, которая регистрирует время выполнения, 
# аргументы и возвращаемое значение функции в файл.
import time
x = input("Enter x value\n")
y = input("Enter y value\n")


def registration(func):
    def wrapper(x,y):
        start = time.time()
        res = func(x,y)
        end = time.time()
        with open("reg.txt", "w")as file:
            file.write(f" execution time: {end-start} seconds\n arguments: {x}, {y}\n return value: {res}")
        return res
    return wrapper

@registration
def sum_num(x,y):
    try:
        return int(x)+int(y)
    except ValueError:
        print("Enter only numbers")
sum_num(x,y)
