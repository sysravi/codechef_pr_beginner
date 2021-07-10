for _ in range(int(input())):
    x = int(input())
    count = 0
    for i in range(11,-1,-1):
        if x>0:
            reduc = x%2**i
            count += x//2**i
            x = reduc
    print(count)
