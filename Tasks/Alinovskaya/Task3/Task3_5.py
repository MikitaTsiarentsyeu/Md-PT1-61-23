# 5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.
list_str = "abcFgirtoksk lEefklFodfkHa kfRTmimxOWcey rZKer qq g gdfgfddDVdddd epWnaEutLbgm eeeeeeEEEEEeeeeeeeeeeeeeeeeeeeeee R";
list_result =[];
split_list_str = list_str.split(' ');

for elem in split_list_str:
    if len(elem) > 5:
        list_result.append(elem);

print(f"list with all strings that have a length greater than 5 characters {list_result}");