# Write a program that takes a list of numbers as input and returns the largest prime number in the list.
input_user = input("Enter numbers seperated by a space \n > ")
input_user = [int(numbers) for numbers in input_user.split()]
#input_user = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prime_nums = []
for x in input_user:

    isPrime = True
    if x > 1:
        for y in range(2, x):
            if x % y == 0:
                isPrime = False
        if isPrime:
            prime_nums.append(x)
prime_nums = sorted(prime_nums)
largest_prime_num = prime_nums[-1]
print(f"The largest prime number is {largest_prime_num} in the list")
