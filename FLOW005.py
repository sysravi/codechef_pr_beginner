for _ in range(int(input())):
    x = int(input())
    count = 0
    count += x//100
    x = x%100
    count += x//50
    x = x%50
    count += x//10
    x = x%10
    count += x//5
    x = x%5
    count += x//2
    x = x%2
    count += x
    print(count)
