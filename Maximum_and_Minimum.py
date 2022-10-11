n = int(input())
m = list(map(int,input().split()))
s = list(set(m))
k = []
for i in s:
    if(m.count(i))==i:
        k.append(i)
if len(k)==0:
    print(-1)
else:
    print(min(k),max(k))