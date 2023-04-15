# 9. Write a recursive function to calculate the power of a given number.
base = 2
exp = 8
def calculate_power(base, exp, result = 1):
    result *= base
    if exp == 1:
        return result
    return calculate_power(base, exp - 1, result)
print(calculate_power(base, exp))
