# -*- coding: utf-8 -*-
import  random
# Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

#test
def random_generator():
    list1 = [0, 1, 2, 3, 4, 7, 8, 10]
    list2 = [4, 7, 10]
    list3 = [2, 3, 8, 9]
    while True:
        yield random.choice(random.choice([list1, list2, list3]))

num = random_generator()
print(next(num))
test = [next(num) if x%2==0 else x for x in range(random.randint(4,20))]
print(test)