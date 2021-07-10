def chec(a,b):
    if int(a) > int(b):
        return('>')
    elif int(a) < int(b):
        return('<')
    else:
        return('=')

x = int(input())
res = []
for i in range(0,x):
    b, c = input().split()
    res.append(chec(b,c))

for f in res:
    print(f)