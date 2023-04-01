list_numbers = list(map(int, input("Enter numbers separated by a space to complete the entry, press 'Enter'").split()))

total = 0

for number in list_numbers:
    if number % 2 == 0:
        total += number

print(f"The sum of all even numbers is {total}")