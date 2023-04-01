for i in range(1,101):
    res = ""
    if i%3==0:
        res+="FIZZ"
    if i%5==0:
        res+="BUZZ"
    if not res:
        res+=str(i)

    print(res)

print([("FIZZ"*(i%3==0)+"BUZZ"*(i%5==0)) or i for i in range(1,101)])