def str_sumbol(line: str) -> tuple:
    """
    The sum of case characters in a string
    """
    count_upper, count_lower = 0, 0
    for i in line:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
    return count_upper, count_lower


line = input('Enter your string:\n')
sum_sumbol = str_sumbol(line)

print(
    f'Number of uppercase characters: {sum_sumbol[0]}\nNumber of lowercase characters: {sum_sumbol[1]}')
