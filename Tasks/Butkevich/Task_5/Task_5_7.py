# 7. Write a recursive function to check whether a given string is a palindrome.

def palindrom(word):
    if len(word) == 1:
        return f"{word} is a palindrome"
    if word[0] != word[-1]:
        return f"{word} is not a palindrome"
    palindrom(word[1:-1])
    return f"{word} is a palindrome"


print(palindrom(input().lower()))
