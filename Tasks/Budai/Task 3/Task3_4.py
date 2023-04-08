from input_numbers import input_list_of_numbers


def find_max_number(nums):
    max_number = nums[0]
    for n in nums:
        if n > max_number:
            max_number = n
    return max_number


numbers = input_list_of_numbers()

numbers.remove(find_max_number(numbers))

print(f'Second largest number is {find_max_number(numbers)}')
