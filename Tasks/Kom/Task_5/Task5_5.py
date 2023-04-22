# 5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

list1 = [1,2,3,4,9,10,11,15,25,26,27,98,99,101]

def get_ranges(l):
    ranges = []
    start = l[0]
    end = start
    for i in range(1, len(l)):
        if l[i] == end + 1:
            end = l[i]
        else:
            if start == end:
                ranges.append(start)
            else:
               ranges.append(f'{start}-{end}')
            start = end = l[i]
    if start == end:
        ranges.append(start)
    else:
        ranges.append(f'{start}-{end}')
    return ranges

print(', '.join(map(str, get_ranges(list1))))