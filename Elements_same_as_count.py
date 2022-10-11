n = int(input())
m = list(map(int,input().split()))
l1= []
l2 = []
for x in m:
    if x not in l1:
        l1.append(x)
for i in l1:
    s = (m.count(i))
    if s ==i:
        l2.append(i)
if len(l2)>0:
    print(*(l2))
else:
    print('-1')