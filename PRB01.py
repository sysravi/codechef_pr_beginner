def prime(n):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                return False
                exit()
        return True
    else:
        return False
for _ in range(int(input())):
    x = int(input())
    if(prime(x)):
        print("yes")
    else:
        print("no")
