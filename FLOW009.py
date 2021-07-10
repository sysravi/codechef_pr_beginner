for _ in range(int(input())):
    q, p = map(int,input().split())
    if q>1000:
        print(q*p*0.90)
    else:
        print(q*p)
