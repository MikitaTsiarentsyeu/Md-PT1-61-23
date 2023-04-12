def count_number_of_characters_in_cases(s) -> (int, int):
    s = s.replace(' ', '')
    lowercase_count = 0
    uppercase_count = 0
    for c in string:
        if c.isupper():
            uppercase_count += 1
        else:
            lowercase_count += 1
    return lowercase_count, uppercase_count


string = input('Input string: ')
lowercase_chars_count, uppercase_chars_count = count_number_of_characters_in_cases(string)

print(f'{lowercase_chars_count} lowercase characters, {uppercase_chars_count} uppercase characters')
