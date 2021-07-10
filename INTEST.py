a, b = input().split(" ")
x=int(a)
y=int(b)
i=0
for f in range(0,x):
    c = input()
    z = int(c)
    if z%y == 0:
        i=i+1
    else:
        continue
print(i)