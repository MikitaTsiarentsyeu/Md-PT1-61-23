eq = input("Enter the eq in format y=kx+b:\n")
x = int(input("Enter the x value:\n"))

eq = eq.replace(' ','').replace('y=','')

coeff = eq.split('x')
print(coeff)
if coeff[0].isdigit():
    k = int(coeff[0])
else:
    print("invalid k value")
    exit()
if coeff[1].isdigit():
    b = int(coeff[1])
else:
    print("invalid b value")
    exit()

res = k*x+b
print(res)