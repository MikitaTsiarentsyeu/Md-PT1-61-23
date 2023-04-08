user_string = input("Enter text: ")

dict_words = {}

for word in user_string.split():
    if word in dict_words:
        dict_words[word] += 1
    else:
        dict_words[word] = 1

print(dict_words)