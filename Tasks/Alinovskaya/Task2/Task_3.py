from statistics import mean;


#1. Write a program that takes a string as input from a user and returns the number of vowels in the string.
list_str = "abcFgirtoksk lEefklFodfkHa kfRTmimxOWcey rZKer qq g gdfgfddDVdddd epWnaEutLbgm eeeeeeEEEEEeeeeeeeeeeeeeeeeeeeeee R";
# vovels = ['a', 'i' , 'e', 'o' , 'y', 'u'];

# count = 0;

# for i in list_str:
#     for k in vovels:
#         if i == k:
#             count += 1;
# print(f"number of vowels in the string is {count}");


# 2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.
#list_num = [1, 3, 56, 78, 4, 8, 10, 12, 46, 29, 400, 300, 219, 501, 101, 42, 15, 64];
# result_sum = 0;
# for n in list_num:
#     if n % 2 == 0:
#         result_sum += n;
# print(f"the sum of all even numbers is {result_sum}")


# 3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string.

# 4. Write a program that takes a list of numbers as input and returns the second largest number in the list.

# lagest_num = 0;
# second_lagest_num = 0;

# for num in list_numbers:
#     if num > lagest_num:
#         lagest_num = num;

# delete_lagest_num = list_numbers.remove(lagest_num);

# for n in list_numbers:
#     if n > second_lagest_num:
#        second_lagest_num = n;

# print(f"second largest number is {second_lagest_num}");


# 5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.

# list_result =[];
#split_list_str = list_str.split(' ');

# for elem in split_list_str:
#     if len(elem) > 5:
#         list_result.append(elem);

# print(f"list with all strings that have a length greater than 5 characters {list_result}");


# 6. Write a program that takes a string as input and returns the string with all vowels removed.
# l = []
# print(f"split_list_str {split_list_str}");
# for elem in split_list_str:
#     elem_split = list(elem);
#     count = 1;
#     print(count)
#     for e in elem_split:
#         if e in vovels:
#             count += 1;
#             continue;
#         else:
#             l.append(e);
#             count += 1;      
#         print(count);
#         print(f"длинна эелемента {(len(elem_split))}")
#         if count == len(elem_split)-1:
#             l.append(' ');

# print(''.join(l));

# 7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.
# list_str_converted = [];
# for b in list_str:
#     if b == b.lower():
#         up = b.upper();
#         list_str_converted.append(up);
#     else:
#         low = b.lower();
#         list_str_converted.append(low);
# print(f"string converted {''.join(list_str_converted)}");

# 8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
#average = mean(list_num);
#print(f"the average of all numbers in the list is {average}");

# 9. Write a program that takes a string as input and returns the string reversed.
list_str_reversed = list_str [:: -1];
print(list_str_reversed);
# 10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.

# You can ask a user for lists to be inputed in the classic Python syntax style or element by element.

# All parts should be done as a separate .py files with names like "Task3_N.py" where N is a number of a part.