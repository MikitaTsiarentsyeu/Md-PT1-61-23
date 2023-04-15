
def power(n):
    def inner(k):
        return k**n
    return inner

sq = power(2)
print(sq(4))

cb = power(3)
print(cb(4))

powers = []
for i in range(1,11):
    powers.append(power(i))

print(powers)

for p in powers:
    print(p(2))

