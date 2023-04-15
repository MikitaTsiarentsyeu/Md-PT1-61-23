def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


string = input('Input string: ')

print("It's a palindrome" if is_palindrome(string) else "Not a palindrome")


