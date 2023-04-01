# 4. Write a program that takes a list of numbers as input and returns the second largest number in the list.

list_num = [1, 3, 56, 78, 4, 8, 10, 12, 46, 29, 400, 300, 219, 501, 101, 42, 15, 64];
lagest_num = 0;
second_lagest_num = 0;

for num in list_num:
    if num > lagest_num:
        lagest_num = num;

delete_lagest_num = list_num.remove(lagest_num);

for n in list_num:
    if n > second_lagest_num:
       second_lagest_num = n;

print(f"second largest number is {second_lagest_num}");