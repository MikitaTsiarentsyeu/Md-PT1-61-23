# 3. Write a function that takes a list of integers as input and returns the sum of all even numbers in the list.
# Handle the TypeError and return "Invalid input type" if the input is not a list or not every element is int.

def sum_all_even_number_in_list(lst: list) -> list:
    try:
        lst = list(map(int, lst))
        return sum(list(filter(lambda i: i % 2 == 0, lst)))
    except TypeError:
        return "Invalid input type"
    except Exception:
        return "Data inputting error"


print(sum_all_even_number_in_list(map(int, input().split())))

