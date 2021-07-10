def rev(n):
    b = int(n)
    rnum = 0
    while(b>0):
        rem = b%10
        rnum = (rnum*10)+rem
        b = b//10
    return rnum
x=int(input())
res = []
for i in range(0,x):
    y=int(input())
    res.append(rev(y))
for f in res:
    print(f)