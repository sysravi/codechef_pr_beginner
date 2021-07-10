def sm(n):
    return (n*(n+1)/2)
def ssm(m,n):
    for i in range(m):
        n = sm(n)
    return(n)
x = int(input())
for i in range(x):
    b,c = map(int,input().split())
    print(int(ssm(b,c)))
