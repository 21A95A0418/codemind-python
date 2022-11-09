a = list(map(int,input().split(',')))
b = []
c = 0
d = []
for i in a:
    for j in range(1,i+1):
        if i%j==0:
            b.append(j)
            c+=j
    if c in a:
        d.append(i)
        c = 0
    else:
        c=0
e = sorted(d)
if len(d)>0:
    print(*(e))
else:
    print('-1')
        