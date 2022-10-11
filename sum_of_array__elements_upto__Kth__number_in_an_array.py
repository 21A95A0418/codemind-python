n = int(input())
m = list(map(int,input().split()))
k = int(input())
s = []
for i in m:
    s.append(i)
    if i==k:
        break
print(sum(s))