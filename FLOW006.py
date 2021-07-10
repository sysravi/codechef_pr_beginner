x = input()
a = int(x)
res = []
s = 0
def getsum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum
for i in range(0,a):
    y = input()
    res.append(getsum(y))
for r in res:
    print(r)
