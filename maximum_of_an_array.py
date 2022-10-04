n = int(input())
m = list(map(int,input().strip().split()))
s = []
for i in range(len(m)):
    s.append(m[i])
print(max(s))