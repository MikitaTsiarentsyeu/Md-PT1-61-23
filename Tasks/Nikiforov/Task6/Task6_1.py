# 1. Write a function that takes two numbers as input and returns their division. 
# Handle the ZeroDivisionError and return "Cannot divide by zero" if the denominator is zero.

def division(a, b):
    try:
        a, b = int(a), int(b)
        prod = a/b
        print(prod)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except:
        print("Something went wrong")

division(input('Enter 1st number:\n'), input('Enter 2nd number:\n'))
    

    