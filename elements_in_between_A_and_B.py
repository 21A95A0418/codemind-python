a = int(input())
b = list(map(int,input().split()))
c,d = map(int,input().split())
e = []
f = 0
for i in b:
    if i>=c and i<=d:
        e.append(i)
        f += 1
if len(e)>0:
    print(*e)
else:
    print('-1')