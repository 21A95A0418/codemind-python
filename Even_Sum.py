n=int(input())
m=list(map(int,input().strip().split()))
d=0
for i in range(len(m)):
    if m[i]%2==0:
        d+=m[i]
print(d)