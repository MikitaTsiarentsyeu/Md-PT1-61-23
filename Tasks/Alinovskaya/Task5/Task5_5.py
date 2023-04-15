# 5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
def get_ranges(l):
    result = []
    start = end = l[0]
    for i, num in enumerate(l):
        if i >  0:
            if num == end + 1:
                end = num
            else:
                result.append(f"{start}-{end}" if start != end else f"{start}")
                start = end = num
        else: continue        
    result.append(f"{start}-{end}" if start != end else f"{start}")
    return ", ".join(result)

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))
