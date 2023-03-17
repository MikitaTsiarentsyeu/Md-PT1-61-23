exchange_rate_dict = {'usd_buy': 2.834, 'usd_sell': 2.838}

print('Choose option: 1 - buy usd, 2 - sell usd')
choice = int(input())

if choice == 1:
    usd_amount = int(input('Enter amount you want to buy: '))
    exchange_rate = exchange_rate_dict.get('usd_sell')
    byn_amount = usd_amount * exchange_rate
    print(f'You will need {(round(byn_amount, 2))} byn')
elif choice == 2:
    usd_amount = int(input('Enter amount you want to sell: '))
    exchange_rate = exchange_rate_dict.get('usd_buy')
    byn_amount = usd_amount * exchange_rate
    print(f'You will get {(round(byn_amount, 2))} byn')
else:
    print('Invalid option!')
