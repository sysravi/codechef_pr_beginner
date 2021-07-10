for _ in range(int(input())):
    b, c = map(int,input().split())
    max = 0
    for _ in range(c,b+1):
        i = int(b%c)
        if(max<i):
            max = i
        if(c<max):
            break
    print(max)
