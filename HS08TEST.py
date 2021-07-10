amt=input()
a=int(amt)
bal=input()
b=float(bal)
if a<b:
    if a%5==0:
        print(b-a-0.50)     #successful transaction
    else:
        print(b)            #incorrect withdrawal amt
else:
    print(b)                #insufficient funds