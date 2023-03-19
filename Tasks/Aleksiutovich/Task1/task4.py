from decimal import Decimal
#Write a program that converts some amount of money from USD to BYN, the amount and ratio are given.
def the_converts_USD_to_BYN():
    print("1 USD = 2.84 BYN")
    x = Decimal(2.84)
    val_USD = Decimal(input("Please enter your amount in USD: "))
    val_BYN = val_USD * x
    print(f"{round(val_USD, 2)} USD = {round(val_BYN, 2)} BYN")
    return val_BYN

the_converts_USD_to_BYN()
