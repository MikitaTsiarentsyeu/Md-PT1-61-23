#  9. Write a recursive function to calculate the power of a given number.

num, pow = 3, 3

def power_of_number(base_numb, power_limit):
    if power_limit == 0:
        return 1
    else:
        return base_numb * power_of_number(base_numb, power_limit - 1)

print(power_of_number(num, pow))