for _ in range(int(input())):
    a = input()
    b = input()
    min = max = 0
    for i in range(len(a)):
        if a[i] == '?' or b[i] == '?':
            max += 1
        elif a[i] != b[i]:
            max += 1
            min += 1
    print(min, ' ', max)
