import random
#Write a program that generates a random number between in a given range, and shows the answer to a user.


def the_generates_random_number():
        lower = int(input("Please enter the lower number: "))
        upper=  int(input("Please enter the upper number:"))
        if lower < upper:
            val_random = random.randint(lower, upper)
            print(f"The number between is {val_random}")
            return val_random
        elif (lower == upper) or (lower > upper):
            print("It is impossible to accept these conditions. Repeat with the correct data")
            return False
        else:
             print("""EROR!!
             REPEAT AGAIN!!!
             Enter only integer numbers!!""")

the_generates_random_number()