r=int(input())
for _ in range(r):
    n=int(input())
    x=input()
    flag=False
    for i in x:
        if i!="N":
            if i=="Y" :
                ntn="NOT INDIAN"
            if i=="I":
                ntn="INDIAN"
            flag=True
            break
    if (flag==False):
        print("NOT SURE")
    else:
        print(ntn)
