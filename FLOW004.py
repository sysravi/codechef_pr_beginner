def sumrev(n):
    num = int(n)
    reverse = n[::-1]
    rev = int(reverse)
    first = rev%10
    last = num%10
    tot = first+last
    return(tot)
x = input()
a = int(x)
lst = []
for i in range(0,a):
    z = input()
    lst.append(sumrev(z))
for f in lst:
    print(f)