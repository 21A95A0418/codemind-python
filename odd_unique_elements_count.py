n = int(input())
m = list(map(int,input().split()))
a = []
for i in m:
    if i%2!=0:
        a.append(i)
c = len(set(a))
print(c)
