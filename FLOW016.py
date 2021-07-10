def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a

def lcm(a, b):
    ans = (a*b)//gcd(a,b)
    return ans

x = int(input())
l1 = []
l2 = []
for i in range(x):
    y, z = input().split()
    b = int(y)
    c = int(z)
    l1.append(lcm(b, c))
    l2.append(gcd(b, c))
for f in range(x):
    print(l2[f],l1[f])
