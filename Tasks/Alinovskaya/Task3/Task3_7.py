# 7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.
list_str_converted = [];
list_str = "abcFgirtoksk lEefklFodfkHa kfRTmimxOWcey rZKer qq g gdfgfddDVdddd epWnaEutLbgm eeeeeeEEEEEeeeeeeeeeeeeeeeeeeeeee R";

for elem in list_str:
    if elem == elem.lower():
        up = elem.upper();
        list_str_converted.append(up);
    else:
        low = elem.lower();
        list_str_converted.append(low);

print(f"string converted {''.join(list_str_converted)}");