n = int(input())
m = list(map(int,input().split()))
k = []
a = 0
for i in m:
    if i%2!=0:
        k.append(i)
for j in k:
    if(m.index(j))%2!=0:
        a+=0
    else:
        a+=1
print(a==0)
    