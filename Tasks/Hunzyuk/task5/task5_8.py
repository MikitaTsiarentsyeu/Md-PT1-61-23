string = input('Enter the string: ')
symbol = input('Enter the symbol: ')


def count_symbols(string, count):
    if len(symbol) > len(string):
        return f'character not found'
    count = 0
    if string.find(symbol) != -1:
        count = 1 + count_symbols(string[string.find(symbol) + 1:], symbol)
    return count

print(count_symbols(string, symbol))
    