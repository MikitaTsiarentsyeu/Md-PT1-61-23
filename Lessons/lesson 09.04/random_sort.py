import random

l = [5,3,7,9,8,65,3,45,88,9,54]

k = 5
m = 3

l[k], l[m] = l[m], l[k]
print(l)

def random_sort(l:list) -> None:
    count = 0
    while not is_sorted(l):
        swap(l)
        count += 1
    print(count)

def is_sorted(l:list) -> bool:
    # return l == sorted(l) takes too much time
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False 
    return True

def swap(l: list) -> None:
    k = generate_index(len(l))
    m = k
    while k == m:
        m = generate_index(len(l))
    l[k], l[m] = l[m], l[k]

def generate_index(n:int) -> int:
    return random.randint(0,n-1)

l = [3,2,5,7,4,1,6]
random_sort(l)
print(l)