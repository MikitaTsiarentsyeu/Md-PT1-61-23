#5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, 
# check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

list = [1, 3, 4, 5, 7, 8, 9]
new_list = []

def look_for_ranges(list):
    start = end = list[0]  
    for num in list[1:]:  
        if num == end + 1: 
            end = num  
        else:  
            new_list.append(f"{start}-{end}" if start != end else f"{start}")  
            start = end = num 
    new_list.append(f"{start}-{end}" if start != end else f"{start}")  
    return ", ".join(new_list)  


# #checking according to task
# list = [0, 1, 2, 3, 4, 7, 8, 10]
# print(look_for_ranges(list))

# list = [4,7,10]
# print(look_for_ranges(list))

# list = [2, 3, 8, 9]
# print(look_for_ranges(list))
