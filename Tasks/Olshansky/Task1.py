# subtask 1
temp_in_celsius=15.5
temp_in_fahrenheit=temp_in_celsius*(9/5)+32
print('temperature: ',round(temp_in_fahrenheit,2),'°F')

# subtask 2
import math

circle_radius=35
circle_area=math.pi*circle_radius**2
print('circle area: ', round(circle_area,2))

# subtask 3
speed_in_kmph=40
speed_in_mps=(speed_in_kmph*1000)/3600
print('speed: ', round(speed_in_mps,2), 'M/S')

# subtask 4
amount_in_USD=100
rate_USD_to_BYN=2.85
amount_in_BYN=amount_in_USD*rate_USD_to_BYN
print('amount:', round(amount_in_BYN,2), 'BYN')

# subtask 5
import random
print('your random number is: ', random.randrange(5,78))