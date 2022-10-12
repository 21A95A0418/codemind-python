n = int(input())
m = list(map(int,input().split()))
k = []
for i in m:
    num = i
    cnt = 0
    for j in range(1,num+1):
        if num%j==0:
            cnt += 1
    if cnt==2:
        k.append(i)
z = (sum(k)/len(k))
print('{:.2f}'.format(z))
    