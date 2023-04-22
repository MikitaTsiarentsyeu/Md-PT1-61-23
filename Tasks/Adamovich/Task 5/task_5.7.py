#7. Write a recursive function to check whether a given string is a palindrome.

my_str = "mamamam"

def palindrome(my_str):
    if len(my_str) == 0 or len(my_str) == 1: # граничный случай
        return True
    else: # рекурсивный случай
        head = my_str[0]
        middle = my_str[1:-1]
        end = my_str[-1]
        return head == end and palindrome(middle)
    

print(palindrome(my_str))
