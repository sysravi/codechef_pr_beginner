for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    l.sort()
    if l[0]==l[1] and l[2]==l[3]:
        print("YES")
    else:
        print("NO")
