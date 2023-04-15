# 7. Write a recursive function to check whether a given string is a palindrome.

text = 'оселоколесо'

def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

    
print(is_palindrome(text))

