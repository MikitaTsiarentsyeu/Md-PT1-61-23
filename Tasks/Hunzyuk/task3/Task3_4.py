list_numbers = list(set(map(int, input("Enter numbers separated by a space to complete the entry, press 'Enter'").split())))
list_numbers.sort()

print(f"Second largest number {list_numbers[-2]}")