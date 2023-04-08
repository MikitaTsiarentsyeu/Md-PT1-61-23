s = input()
count = 0

for i in range (len(s)):
    if s[i] in 'а,у,о,ы,э,я,ю,ё,и,е' :
        count += 1
print('Количество гласных букв равно:', count)       




