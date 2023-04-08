#1. Write a program that converts Celsius to Fahrenheit
value_in_Celsius = 10
value_in_Fahrenheit = (value_in_Celsius * 1.8) + 32
print(value_in_Fahrenheit)

#with user's interaction
input_value_in_Celsius  = int(input("Input integer value in Celsius: "))
value_in_Fahrenheit = int((input_value_in_Celsius * 1.8) + 32)
print(f'{input_value_in_Celsius}{chr(176)}C is {value_in_Fahrenheit}{chr(176)}F')