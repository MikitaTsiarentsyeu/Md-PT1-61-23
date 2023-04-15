# 5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for
# those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"


def my_range(lst_num):
    l = []
    first = last = lst_num[0]
    for i, j in enumerate(lst_num):
        if i > 0:
            if j == last + 1:
                last = j
            else:
                l.append(f"{first}-{last}" if first != last else f"{first}")
                first = last = j
        else:
            continue
    l.append(f"{first}-{last}" if first != last else f"{last}")
    return ", ".join(l)


lst_num = list(set(map(int, input().split())))
lst_num.sort(reverse=False)
print(my_range(lst_num))
