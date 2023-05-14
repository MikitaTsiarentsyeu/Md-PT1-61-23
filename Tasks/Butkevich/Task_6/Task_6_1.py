# 1. Write a function that takes two numbers as input and returns their division. Handle the ZeroDivisionError
# and return "Cannot divide by zero" if the denominator is zero.

def division(num_1: int, num_2: int) -> int:
    try:
        try:
            return int(num_1) / int(num_2)

        except ZeroDivisionError:
            return "Cannot divide by zero"
    except Exception:
        return "you entered no number of type int"


print(division(input(), input()))
