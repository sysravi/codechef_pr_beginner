x = input()
a = int(x)
res = []
for i in range(0,a):
    y, z = input().split()
    b = int(y)
    c = int(z)
    fin = b+c
    res.append(fin)
for d in res:
    print(d)
