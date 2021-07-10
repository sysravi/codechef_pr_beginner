def help(z):
    if z <10:
        return(True)
    else:
        return(False)
x = int(input())
s = "Thanks for helping Chef!"
res = []
for i in range(0,x):
    b = int(input())
    if help(b):
        res.append(s)
    else:
        res.append(-1)

for f in res:
    print(f)