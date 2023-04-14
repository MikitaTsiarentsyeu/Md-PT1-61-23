# 7. Write a recursive function to check whether a given string is a palindrome.
str = "anna"
def check_palindrom(str, count = 1, result = []):
    elem = list(str) 
    elem_reverse = list(reversed(str))
    result.append(elem_reverse[count-1])
    if count == len(str):
        if elem ==  result:
            return True
        else:
            return False
    return check_palindrom(str, count + 1)    
print(check_palindrom(str));
