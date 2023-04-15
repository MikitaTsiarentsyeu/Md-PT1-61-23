def revers_str(str: str, i: int) -> str:
    """
    Inverted string using recursion
    """
    if i != 0:
        print(str[i-1], end='')
        i -= 1
        return revers_str(str_out, i)


str_out = input('Enter your string:\n')
i = len(str_out)

revers_str(str_out, i)
