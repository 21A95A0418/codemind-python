n = int(input())
m = list(map(int,input().strip().split()))
k = 0
for i in range(len(m)):
    if i%2==0:
        k += m[i]
print(k)
        