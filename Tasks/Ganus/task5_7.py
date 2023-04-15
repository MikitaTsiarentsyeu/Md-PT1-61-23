def palindrome_reverse(a):
    a = a.lower()
    a = a.replace(" ", "")
    if len(a) == 0:
        return ""
    else:
        return a[-1] + palindrome_reverse(a[:(len(a)-1)])
def palindrome_straight(a):
    a = a.lower()
    a = a.replace(" ", "")
    if not a:
        return ""
    else:
        return a[0] + palindrome_straight(a[1:])
def palindrome(func1, func2):
    if func1 == func2:
        return "Данная строка является палиндромом"
    else:
        return "Данная строка не является палиндромом"

a = "Молебен о коне белом"
print(palindrome(palindrome_reverse(a), palindrome_straight(a)))
a = "Котики любят рыбку"
print(palindrome(palindrome_reverse(a), palindrome_straight(a)))

    