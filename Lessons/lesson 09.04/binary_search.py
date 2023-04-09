l = [1,2,3,4,5,6,7,8,9,10]

target = 7

def search(l, target, low, high):
    if high >= low:
        mid = (low + high) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            return search(l,target, low, mid-1)
        else:
            return search(l,target, mid+1, high)
    else:
        return -1

print(search(l, 100, 0, len(l)-1))