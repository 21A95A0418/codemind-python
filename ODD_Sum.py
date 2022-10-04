n=int(input())
m=list(map(int,input().strip().split()))
f = 0
for i in range(len(m)):
    if m[i]%2!=0:
        f += m[i]
print(f)