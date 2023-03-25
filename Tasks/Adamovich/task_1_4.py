#4 Write a program that converts some amount of money from USD to BYN, the amount and ratio are given.
import decimal
dollars_per_byn = decimal.Decimal("2.4")
dollars_count = decimal.Decimal(input("Input amount in dollars: "))
byn_count = dollars_count * dollars_per_byn
print(f" {dollars_count} $ is {byn_count} BYN ")
print(byn_count)