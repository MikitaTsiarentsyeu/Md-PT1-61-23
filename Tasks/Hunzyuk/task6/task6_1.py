def division_two_numbers(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        return f"Cannot divide by zero"

print(division_two_numbers(10, 0))