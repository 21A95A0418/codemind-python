a = int(input())
b = list(map(int,input().split()))
d = 0
e = 0
for i in b:
    for j in range(1,i+1):
        if i%j==0:
            d += 1
    if d==2:
        e+=1
        d = 0
    else:
        d = 0
print(e)
