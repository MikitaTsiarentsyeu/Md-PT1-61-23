# 9. Write a recursive function to calculate the power of a given number.

def the_power_of_a_given_number(num, power):
    if power == 0:
        return 1
    return num * the_power_of_a_given_number(num, power - 1)


print(the_power_of_a_given_number(int(input()), int(input())))
