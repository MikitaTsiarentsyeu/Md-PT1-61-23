#8. Write a recursive function to count the number of occurrences of a given character in a string.

text = 'у пруда в траве во мраке шуршат раки в шумной драке'

def count_of_occurrences(str, char):
    if len(str) == 0:
        return 0
    else:
        if str[0] == char:
            return 1 + count_of_occurrences(str[1:], char)
        else:
            return count_of_occurrences(str[1:], char)
    
        
print(count_of_occurrences(text, 'р'))
            
