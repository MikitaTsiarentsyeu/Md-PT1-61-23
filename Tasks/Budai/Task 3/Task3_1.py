vowels = 'aeiouy'
string = input('Input string: ')
count_vowels = 0

for c in string:
    if c.lower() in vowels:
        count_vowels += 1

print(f'There are {count_vowels} vowels in your string')
