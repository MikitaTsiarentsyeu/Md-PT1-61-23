string = input('Input text: ')
words = string.split()
words_count_dict = {}

for word in words:
    if word in words_count_dict:
        words_count_dict[word] += 1
    else:
        words_count_dict[word] = 1

print(words_count_dict)
