#4.Write a program that converts some amount of money from USD to BYN, the amount and ratio are given.
from bs4 import BeautifulSoup     
from urllib.request import urlopen   

web_page = urlopen('https://myfin.by/bank/kursy_valjut_nbrb')
soup = BeautifulSoup(web_page)
tags = soup.find_all('td')
Curr = float(tags[1].text)
UsdAmount = float(input("How many USD do you want to convert?:"))
BynAmount = round((UsdAmount * Curr), 4)

print(f"{UsdAmount} USD is {BynAmount} BYN")                
