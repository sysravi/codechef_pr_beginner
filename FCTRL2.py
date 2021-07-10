def factorial(n):
    x = n
    for i in range(1,n):
        x = x*(n-i)
    return x
b = input()
y = int(b)
res = []
for z in range(0,y):
    f = input()
    c = int(f)
    res.append(factorial(c))

print("\n")
for m in res:
    print(m)