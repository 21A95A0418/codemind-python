n = int(input())
m = list(map(int,input().strip().split()))
a = 0
b = 0
c = 0
for i in range(len(m)):
    if m[i]%2==0:
        a += m[i]
    else:
        b += m[i]
print(abs(a-b))