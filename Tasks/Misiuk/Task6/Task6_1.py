def division_func(num1: str, num2: str) -> int:
    """
    Function for dividing two numbers 
    with error handling when dividing by zero.
    """
    while True:
        if num1 == 'n' or num2 == 'n':
            return 'Exit this program!!!'
        try:
            res = int(num1) // int(num2)
            return f'{num1} divided by {num2} = {res}'
        except ZeroDivisionError:
            print("Can't divide by zero!!!")
            num2 = (input('Enter the divisor again:\n'))
        except:
            print('You have entered non-numeric values, please enter all values again or type n to exit the program!!!')
            num1 = input('Enter the first number:\n')
            num2 = input('Enter the second number:\n')


num1 = input('Enter the first number:\n')
num2 = input('Enter the second number:\n')

print(division_func(num1, num2))
