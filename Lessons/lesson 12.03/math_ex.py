x, y = 2, 7

print(y**x)
print(y%x)
print(y/x)
print(y//x)

print(x*y)
print(x+y)
print(y-x)

print((2*6)//(2+2))

print(x!=y)
print(x==y)

#test comment

print(type(3))
x = int(-2.8)
print(type(x), x)

print(round(3.5))
print(round(4.5))
print(round(5.5))
print(round(6.5))

print(type(3.5))

print(1.1+1.1+1.1)

import decimal
x = decimal.Decimal(1.1)
print(x+x+x)
print(x)

import math
print(math.sqrt(144))
print(math.sin(2*math.pi))

import random
print(random.randint(0,10))
print(random.choice("test"))