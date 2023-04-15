def list_strings_revers(a: list) -> list:
    new_list = []
    for i in a:
        i = i[::-1]
        new_list.append(i)
    return new_list

a = ["frost", "happy", "day", "monday"]
print(list_strings_revers(a))

