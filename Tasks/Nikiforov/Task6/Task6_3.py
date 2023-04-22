# 3. Write a function that takes a list of integers as input and returns the sum of all even numbers in the list.
# Handle the TypeError and return "Invalid input type" if the input is not a list or not every element is int.

def sum_of_even():
    l = input("Enter a list of integers:\n").strip().split(" ")
    try:
        l = list(map(int, l))
        sum = 0
        for el in l:
            if el % 2 == 0:
                sum += el
        return sum
    except TypeError:
        return "Invalid input type"
    except:
        return "Something went wrong"

print(sum_of_even())

