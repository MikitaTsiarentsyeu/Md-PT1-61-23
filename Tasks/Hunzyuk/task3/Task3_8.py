list_numbers = list(map(int, input("Enter numbers separated by a space to complete the entry, press 'Enter'").split()))

print(f"The average value of the numbers in the sheet is {sum(list_numbers) / len(list_numbers)}")