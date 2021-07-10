def chk(n):
    if(n==n[::-1]):
        return("wins")
    else:
        return("loses")
for _ in range(int(input())):
    x = input()
    print(chk(x))
