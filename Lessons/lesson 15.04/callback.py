import threading

def apply(l, func):
    for i in l:
        func(i)

apply([1,2,3,4,5], print)

def test_callback():
    print("hello, it's me")

threading.Timer(1, test_callback).start()
for i in range(3750):
    print(i)