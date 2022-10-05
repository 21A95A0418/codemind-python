n = int(input())
m = list(map(int,input().split()))
k = []
o = []
for i in range(n):
    for x in m:
        if x%2!=0:
            k.append(int(x))
        else:
            o.append(x)
    break
print(*(k+o))