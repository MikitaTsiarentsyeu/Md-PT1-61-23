x = "my test string"
print(type(x))

y = 'test'
print("test"=='test')

"this is only a 'test'"

x = '''my first line
my second line
my third line'''

print(repr(x))

s = "me very long string"
print(len(s))
print(len(''))
print(len(' '))
print(len('\n'))

print(s[0], s[1], s[2], s[3], s[4], s[5])
print(s[0], s[-1], s[-2], s[-3], s[-4], s[-5])
print(s[len(s)-1])

print(s[3:-3:2])
print(s[::-1])