string = input('Enter the string: ')

def is_polindrom(string):
    if len(string) < 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_polindrom(string[1:-1])
        else:
            return False
        
print(is_polindrom(string))

