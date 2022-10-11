n = int(input())
m = list(map(int,input().split()))
z = int(input())
s = set(m)
c = []
for i in s:
    if m.count(i)==z:
        c.append(i)
if len(c)>0:
    print(*(c))
else:
    print('-1')