strings = list(map(str, input('Enter strings: ').split()))

strings_longer_than_five = [s for s in strings if len(s) > 5]

print('Strings with length more than 5:')
print(strings_longer_than_five)
