def string_palindrome(st: str) -> str:
    """
    Search for a palindrome string
    """
    if len(st) < 1:
        return f'String is a palindrome!'
    else:
        if st[0] == st[-1]:
            return string_palindrome(st[1:-1])
        else:
            return f"String isn't a palindrome!"


str_input = input("Enter string:\n")

print(string_palindrome(str_input))
