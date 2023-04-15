def fibinacci(n: int) -> int:
    """
    Searching for the fibonacci number
    """
    if n < 0:
        print('Incorrect input')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibinacci(n-1) + fibinacci(n-2)


num_input = int(input('Enter your number:\n'))
print(f'{num_input} - {fibinacci(num_input)} the fibonacci number ')
