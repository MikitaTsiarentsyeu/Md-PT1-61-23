def exponentiation(num: int, degree: int) -> int:
    """
    Exponentiation function
    """
    if degree != 0:
        return num * exponentiation(num, degree-1)
    else:
        return 1


num_input = int(input('Enter your number:\n'))
degree = int(input('Enter your degree:\n'))

print(
    f'The number {num_input} raised to the power of {degree} is {exponentiation(num_input,degree)}')
