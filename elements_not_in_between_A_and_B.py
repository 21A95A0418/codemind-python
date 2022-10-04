n = int(input())
m = list(map(int,input().split()))
a,b = map(int,input().split())
s = []
d = 0
for i in m:
    if i<a or i>b:
        s.append(i)
        d = 1
if d==1:
    print(*s)
else:
    print(-1)