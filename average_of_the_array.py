n=int(input())
m=list(map(int,input().strip().split()))
h = 0
for i in range(len(m)):
    h += m[i]
k=h/len(m)
print('{:.2f}'.format(k))