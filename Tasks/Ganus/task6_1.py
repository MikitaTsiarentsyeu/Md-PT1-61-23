def division(a, b):
    try:
        
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
        
a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))
division(a, b)
