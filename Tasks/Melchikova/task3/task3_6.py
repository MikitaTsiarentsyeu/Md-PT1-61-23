def list(text):
    to_remove = 'AEIOUaeiou'
    result = ''
    for letter in text:
        if letter not in to_remove:
            result += letter
    return result
print(list('Hello world'))
