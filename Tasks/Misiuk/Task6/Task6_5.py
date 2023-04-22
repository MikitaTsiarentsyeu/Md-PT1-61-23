cache = dict()


def get_cache(func):
    def wrapper(*args):
        key = str(args)
        if key in cache:
            return cache[key]
        else:
            res = func(*args)
            cache[key] = res
        return res
    return wrapper


@get_cache
def sum_num(num1: int, num2: int) -> int:
    return num1 + num2


@get_cache
def firs_last_word(line: str) -> str:
    line = line.split()
    return line[0], line[-1]


@get_cache
def line_length(line: str) -> int:
    line = line.split()
    return len(line)


sum_num(10, 15)

firs_last_word('This test string')
firs_last_word('This test string')

sum_num(10, 1)
sum_num(10, 25)
sum_num(10, 15)
sum_num(10, 15)
sum_num(10, 15)
sum_num(15, 10)


line_length(
    'This is a test string to test the operation of a function that returns')

line_length(
    'This is a test string to test the operation of a function that returns')

print(cache)
