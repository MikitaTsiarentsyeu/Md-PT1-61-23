amount_USD = float(input("Enter the amount in US dollars: "))
course_BYN = float(input("Enter the exchange rate of the Belarusian ruble to the dollar: "))

amount_BYN = amount_USD * course_BYN

print(f"The amount in Belarusian rubles is equal to {round(amount_BYN, 2)}")