# 10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.
list_num = [1, 3, 56, 78, 4, 8, 10, 12, 46, 29, 400, 300, 219, 501, 101, 42, 15, 64];
list_prime_numbers = [];
result = 0;

for num in list_num:
        if num == 1:
             continue;
        count = 0;
        d = 2;
        while d < num:
            if num % d == 0:
                count += 1
            d += 1;
        if count == 0:
            list_prime_numbers.append(num)
for elem in list_prime_numbers:
     if elem > result:
          result = elem;

print(f"the largest prime number in the list is {result}");
# print(max(list_prime_numbers))