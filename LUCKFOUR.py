x = int(input())
res = []
for i in range(0,x):
    count=0
    y = input()
    b=list(y)
    for f in b:
        if f=="4":
            count=count+1
    res.append(count)
for l in res:
    print(l)