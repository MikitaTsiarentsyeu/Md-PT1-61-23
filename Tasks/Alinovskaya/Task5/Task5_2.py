# 2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.
def reverse_list (list_of_string, sp = ''):
    new_list = []
    for i in list_of_string:
        elem = list(i)
        elem.reverse()
        elem_for_new_list = []
        for k in elem:
            elem_for_new_list.append(k)
        new_list.append(sp.join(elem_for_new_list))
    return new_list
print(reverse_list(['Windows', 'macOS', 'Linux']))
