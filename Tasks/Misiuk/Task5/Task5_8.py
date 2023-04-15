def search_target(text: str, target: str) -> int:
    """
    Search for the number of occurrences of a letter in a string
    """
    if not text:
        return 0
    if text[0] == target:
        return 1 + search_target(text[1:], target)
    return search_target(text[1:], target)


text_input = input('Enter your string:\n')
target = input('Enter character to search:\n')
output = search_target(text_input, target)

print('--------------------------------')
print(f'Text: {text_input}\nTarget: {target}')
print('--------------------------------')
print(f'Number of occurrences in a string: {output}\n')
