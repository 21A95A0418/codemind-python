n = int(input())
m = list(map(int,input().split()))
c = []
for i in range(0,n):
    for i in m:
        if i%2!=0:
            c.append(i)
print(c[-1])