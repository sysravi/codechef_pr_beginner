n = int(input())
sol=[]
odd = 0
even = 0
sol = list(map(int,input().split()))
for i in sol:
    if i%2==0:
        even+=1
    else:
        odd+=1
if odd>=even:
    print("NOT READY")
else:
    print("READY FOR BATTLE")
