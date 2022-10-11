n = int(input())
m = list(map(int,input().split()))
s = set(m)
c = 0
for i in s:
    if m.count(i)==i:
        c += 1
print(c)