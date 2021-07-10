x = int(input())
p1 = True
s = 0
t = 0
max_lead = 0
for i in range(x):
    a, b = input().split()
    y = int(a)
    z = int(b)
    s += y
    t += z
    if s>t:
        c = s-t
        if c>max_lead:
            p1 = True
            max_lead = c
    else:
        d = t-s
        if d>max_lead:
            p1 = False
            max_lead = d
if p1:
    print(1,' ',max_lead)
else:
    print(2,' ',max_lead)
