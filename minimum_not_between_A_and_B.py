a = int(input())
b = list(map(int,input().split()))
c,d = map(int,input().split())
e = []
f = []
for i in b:
    if i>=c and i<=d:
        e.append(i)
    else:f.append(i)
if len(f)>0:
    print(min(f))
else:print('-1')