n = int(input())
m = list(map(int,input().split()))
k = []
for i in range(0,n):
    for j in m:
        if j%2==0:
            k.append(j)
print(k[-1])