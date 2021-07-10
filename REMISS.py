x = int(input())
min = []
max = []
for i in range(0,x):
    y, z = input().split()
    a = int(y)
    b = int(z)
    if a>b:
        min.append(b)
    else:
        min.append(a)
    c = a+b
    max.append(c)
for f in range(0,x):
    print(min[i],max[i])
