
s = "the test string"
print(type(s[0]))

print('3' in s) 
print('e' in s) 

print('the' in s) 
print('long' in s) 

print(s.find('e'))
target = 't'
if target in s:
    print("it's in!")
if s.find(target): #use with caution for the 0 index
    print("we found it!")

print(s.find('long'))
print(s.find('test'))

print(s.replace(' ', '-'), s)
test_new_str = s.replace("the", "ThE").replace("t", "T").replace("n", "N")
print(test_new_str)

print(test_new_str.upper())
print(test_new_str.lower())
print(test_new_str.capitalize())
print(test_new_str.title())

culture1 = "en_EN"
culture2 = "fr_FR"
if culture1.lower() == culture2.lower():
    print("it's equal")

test_str = "  some data "
print(test_str.replace(' ', ''))
print(test_str.strip(' '))

res = "test str1" + "test str2" + "test str3"
print(res)

print(5*"test")


c, d, p = "cat", "dog", "parrot"
"a cat, a dog and a parrot"
print("a " + c + ", a " + d + " and a " + p)
"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog and a"
"a cat, a dog and a parrot"

template = "a {animal1}, a {animal2} and a {animal3}"
print(template.format(animal1 = c, animal2 = d, animal3 = p))
# print(template.format(p, c, d))

print(f"a {c}, a {d} and a {p}")
print(25/4.9)
x = 4.9
print(f"the answer is {25/x:.2f}")

print("%s %d" % ("the answer is", 77)) # old style, never use it

"number "+"1"
f"number {1}"

st = "my very long test string"
res = st.split()
print(res)
print(res[0])

print(culture1.split('_'))
print("test test test".split("test"))

res = "/test level1/test level2/test level 3".split('/')
print('\\'.join(res))