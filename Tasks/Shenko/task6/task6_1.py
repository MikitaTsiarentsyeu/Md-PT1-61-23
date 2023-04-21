# Напишите функцию, которая принимает на вход два числа и возвращает их деление.
# Обработайте ZeroDivisionError и верните «Невозможно разделить на ноль», если знаменатель равен нулю. 

x = int(input("Enter x value\n"))
y = int(input("Enter y value\n"))
def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Cannot divide by by zero")
print(division(x,y))