new_dict = {}
def new_decor(func):
    def new_func(*args, **kwargs):
        new_str = ""
        for i in list(args):
            i = str(i)
            new_str += i
        for j in list(kwargs):
            j = str(j)
            new_str += j
        result = func(*args, **kwargs)
        if args in new_dict:
            print(new_dict[new_str])
        else:
            print(result)
            new_dict[new_str] = result
        print(new_dict)
    return new_func

@new_decor
def add_ints(a, b, c, d):
    return a + b + c + d
add_ints(2, 10, 85, 52)
add_ints(15, 40, 25, 100)
add_ints(2, 10, 85, 52)
add_ints(1524, 80, 149, 780)
add_ints(4, 8, 56, 8)
add_ints(2, 10, 85, 52)
