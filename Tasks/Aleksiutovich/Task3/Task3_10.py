# Write a program that takes a list of numbers as input and returns the largest prime number in the list.
input_user = [1, 2, 3, 4, 7, 8, 9]
prime_nums =[]
for x in input_user:

   if x > 2:
       for y in range(2,x):
        if x%y == 0:
            break
        else:
            print(x)

   else:
       continue