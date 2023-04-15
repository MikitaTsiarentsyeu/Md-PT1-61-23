number = int(input('Enter the number: '))

def fibonacci(number):
    if number in (1, 2):
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(number))