n = int(input())
m = list(map(int,input().split()))
m1 = list(set(m))
k = []
for i in m1:
    if(m.count(i))==i:
        k.append(i)
if len(k)==0:
    print(-1)
else:
    x = ((sum(k))/len(k))
    print("{:.2f}".format(x))