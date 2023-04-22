#6. Write a recursive function to reverse a string.

def reversed_string (str):
     if len(str) == 0: # граничный случай
        return str
     else:
        return reversed_string(str[1:]) + str[0]
     
print(reversed_string("summer"))


     
         