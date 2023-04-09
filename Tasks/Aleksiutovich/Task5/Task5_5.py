# -*- coding: utf-8 -*-
import  random
# Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
def get_ranges(*numbers):
    if not numbers:
        return ""
    ranges = []
    start = end = numbers[0]
    for num in numbers[1:]:
        if num == end + 1:
            end = num
        else:
            ranges.append(f"{start}-{end}" if start != end else f"{start}")
            start = end = num
    ranges.append(f"{start}-{end}" if start != end else f"{start}")
    return ", ".join(ranges)
#test
def random_generator():
    list1 = [0, 1, 2, 3, 4, 7, 8, 10]
    list2 = [4, 7, 10]
    list3 = [2, 3, 8, 9]
    while True:
        yield random.choice(random.choice([list1, list2, list3]))
test = [next(random_generator()) for x in range(random.randint(4,20))]
print(test)
print(get_ranges(test))