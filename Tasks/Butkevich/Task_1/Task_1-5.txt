# import math
# import random


# # 1.Write a program that converts Celsius to Fahrenheit.
# def degree(digit):
#     if digit.isdigit():
#         digit = int(digit)
#         return digit * 1.8 + 32
#     return f"{digit} is not digit, enter a number"
#
#
# print(degree(input()))
#
#
# # 2.Write a program that calculates the area of a circle given its radius.
# def area(radius):
#     if radius.isdigit():
#         radius = int(radius)
#         return math.pi * radius ** 2
#     return f"{radius} is not digit, enter a number"

#
# print(area(input()))
# 3.Write a program that converts kilometers per hour to meters per second, given the speed in kilometers per hour.
# class Converts:
#     def __init__(self, kilometers, hours):
#         self.kilometers = kilometers
#         self.hour = hours
#
#     def converts(self):
#         self.meters = self.kilometers * 1000
#         self.second = self.hour * 3600
#         self.speed = self.meters / self.second
#
#         return f"Speed is {self.speed.__round__(2)} meters per second"
#
#
# speed = Converts(int(input()), int(input()))
# print(speed.converts())


# 4.Write a program that converts some amount of money from USD to BYN, the amount and ratio are given.
# def money(sum_usd, dollar_exchange_rate):
#     sum_byn = sum_usd * dollar_exchange_rate
#     return sum_byn.__round__(3)
#
#
# print(money(float(input()), float(input())))
#
#
# 5.Write a program that generates a random number between in a given range, and shows the answer to a user.
# def lucky_number_Slevin(num_1, num_2):
#     if int(num_1) > int(num_2):
#         return f"the number {num_1} greater than the number {num_2} is incorrect sequence"
#     else:
#         return random.randint(int(num_1), int(num_2))
#
#
# print(lucky_number_Slevin(input(), input()))
