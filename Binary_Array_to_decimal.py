n = int(input())
m = list(map(int,input().split()))
k = ''
for i in range(0,n):
    k += str(m[i])
print(int(k,2))