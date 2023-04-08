import pickle

data = {(1,2,3,4,5): "one two three four five", (7,):"seven"}

# data = pickle.dumps(data)
# print(data)

with open('test.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('test.pickle', 'rb') as f:
    data = pickle.load(f)

print(data)

prnt = pickle.dumps(print)
prnt = pickle.loads(prnt)

prnt("I'm the new print")
print("I'm the original print")