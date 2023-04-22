def sum_of_even(nums):
    try:
        return sum(n for n in nums if n % 2 == 0)
    except TypeError:
        return 'Invalid input type'


def input_int_list(message):
    while True:
        try:
            res = [int(n) for n in input(message).split()]
            return res
        except ValueError:
            print('You should enter only integers')
            continue


numbers = input_int_list('Input list of integers separated with space: ')
print(sum_of_even(numbers))
