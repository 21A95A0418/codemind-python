n = int(input())
m = list(map(int,input().strip().split()))
s = 0
for i in range(len(m)):
    s += m[i]
print(s)