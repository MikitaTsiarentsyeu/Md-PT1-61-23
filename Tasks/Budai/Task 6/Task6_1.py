def division(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        return 'Cannot divide by zero'


def input_int(message):
    while True:
        try:
            n = int(input(message))
            return n
        except ValueError:
            print('Input an integer')
            continue


number1 = input_int('Enter the first number: ')
number2 = input_int('Enter the second number: ')

result = division(number1, number2)
print(f'{number1} / {number2} = {result}')
