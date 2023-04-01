#1. Write a program that takes a string as input from a user and returns the number of vowels in the string.
list_str = "abcFgirtoksk lEefklFodfkHa kfRTmimxOWcey rZKer qq g gdfgfddDVdddd epWnaEutLbgm eeeeeeEEEEEeeeeeeeeeeeeeeeeeeeeee R";
vovels = ['a', 'i' , 'e', 'o' , 'y', 'u'];

count = 0;

for i in list_str:
    for k in vovels:
        if i == k:
            count += 1;

print(f"number of vowels in the string is {count}");