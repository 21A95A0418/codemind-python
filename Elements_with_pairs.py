n = int(input())
m = list(map(int,input().split()))
k = []
for i in m:
    k.append(i)
if len(k)%2!=0:
    k.append(0)
print(*k)
        
