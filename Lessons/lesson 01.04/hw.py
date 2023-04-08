s = "bls      khgk ukg lsklhgie        jhof"

s = s.replace(' ', '')

v = []
res = []

for symbol in s:
    if symbol not in v:
        res.append(symbol)

''.join(res)

d = {}

for symbol in s:
    if symbol in d:
        d[symbol] += 1
    else:
        d[symbol] = 1


# viwed = []

# unique = set(s)

# for symbol in s:
    # if symbol not in viwed:
        # print(f"count of the symbol {symbol} is {s.count(symbol)}")
        # viwed.append(symbol)