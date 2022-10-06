n = int(input())
m = list(map(int,input().split()))
k = []
for i in range(0,n):
    if m[i]==1 or m[i]==0:
        k.append(i)
a = len(m)
if len(k)==a:
    print('True')
else:
    print('False')