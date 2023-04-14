
def case_count(string):

    count_upper_case = 0
    count_lower_case = 0

    for letter in string:
        if letter.isupper():
            count_upper_case += 1
        elif letter.islower():
            count_lower_case += 1
    return f'Number of characters in upper case is {count_upper_case}, in lowercase is {count_lower_case}'

print(case_count('UPPER case, lower case'))