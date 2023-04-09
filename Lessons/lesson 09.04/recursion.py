def level1():
    print("start of the level 1")
    level2()
    print("end of the level 1")

def level2():
    print(" start of the level 2")
    level3()
    print(" end of the level 2")

def level3():
    print("     start of the level 3")
    level4()
    print("     end of the level 3")

def level4():
    print("         start of the level 4")
    print("         end of the level 4")

def level(n=0):
    if n == 10:
        return
    print(f"{' '*n}start of the level {n}")
    level(n+1)
    print(f"{' '*n}end of the level {n}")

# level()

# for i in range(10):
    # print(i)

def print_10_times(i=0) -> None:
    if i == 10:
        return
    print(i)
    print_10_times(i+1)

print_10_times()


# 5! = 5*4*3*2*1
# 4! = 4*3*2*1
# 3! = 3*2*1
# 2! = 2*1
# 1! = 1

def factorial(n:int) -> int:
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(1), factorial(2), factorial(3), factorial(4), factorial(5))

# 12345 -> 15

def digit_sum_str(num, i=0, res=0):
    str_num = str(num) if isinstance(num, int) else num
    if i == len(str_num):
        return res
    res += int(str_num[i])
    return digit_sum_str(str_num, i+1, res)

print(digit_sum_str(12345))

def digit_sum(num):
    if num == 0:
        return 0
    rem = num % 10
    return rem + digit_sum(num // 10)

print(digit_sum(12345))

