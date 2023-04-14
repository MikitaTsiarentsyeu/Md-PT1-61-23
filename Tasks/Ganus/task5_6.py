def recursive_reverse(a):
    if len(a) == 0:
        return ""
    else:
        return a[-1] + recursive_reverse(a[:(len(a)-1)])
a = "Светит солнце, поют птицы"
print(recursive_reverse(a))