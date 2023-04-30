# Write a function that takes a list of integers as input and returns the sum of all even numbers in the list. 
# Handle the TypeError and return "Invalid input type" if the input is not a list or not every element is int.

list = []
def number(list, res = 0):
    try:
        for i in list:
            if i % 2 == 0:
                res += i
        return f'Sum of all even numbers in a list - {res}'
    except TypeError:
        return f'Invalid input type'


print(number(["a", 6, 7, 9]))
print(number([10, 6, 7, 9]))
