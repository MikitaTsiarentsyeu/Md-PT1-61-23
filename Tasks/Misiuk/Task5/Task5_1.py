def sum_of_number(num1: int, num2: int) -> int:
    """
    Function sum of number
    """
    return num1 + num2


num1, num2 = input('Enter two integers separated by a space:\n').split(' ')
print(f'The sum is equal: {sum_of_number(int(num1),int(num2))}')
