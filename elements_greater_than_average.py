n = int(input())
m = list(map(int,input().split()))
a =[]
b = 0
d = len(m)
e = 0
for i in range(n):
    for j in m:
        b += int(j)
    break
c = b//n
for k in m:
    if k >= c:
        e += 1
print(e)