for _ in range(int(input())):
    n, m, k = map(int, input() . split())
    while(k):
        if n > m:
            n -= 1
            k -= 1
        elif m > n:
            m -= 1
            k -= 1
        else:
            break
    print(abs(n-m))
