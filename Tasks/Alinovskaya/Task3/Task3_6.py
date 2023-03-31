# 6. Write a program that takes a string as input and returns the string with all vowels removed.
list_str = "aberyyyyqwwwwwwwwwwwwwwwuersaqzeiiiiiiii";
vowels = ['a', 'i' , 'e', 'o' , 'y', 'u'];
list_result = [];

for elem in list_str:
    elem_split = list(elem);
    for e in elem_split:
        if e in vowels:
            continue;
        else:
            list_result.append(e);

print(f"the string with all vowels removed {''.join(list_result)}");        