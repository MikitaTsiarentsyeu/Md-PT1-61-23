def get_strings_with_length_greater_than_five(strings: list) -> list:
    return [s for s in strings if len(s) > 5]


strings = [s for s in input('Input strings separated with space: ').split()]

print(get_strings_with_length_greater_than_five(strings))
