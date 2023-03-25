from decimal import Decimal
print('Введите колличество USD которые хотите перевести в BYN.')
print('Курс на сегодня: 1 USD = 2.85 BYN.')
USD = int(input("Введите сумму: "))
BYN = Decimal('2.85')
output = USD * BYN
print('--------------ИТОГ------------------')
print(f'За {USD}$, вы получите {output} BYN')
