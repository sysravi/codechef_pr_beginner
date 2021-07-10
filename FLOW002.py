x = input()
a = int(x)
res = []
for i in range(0,a):
    y, z = input().split()
    b = int(y)
    c = int(z)
    d = b%c
    res.append(d)
for r in res:
    print(r)