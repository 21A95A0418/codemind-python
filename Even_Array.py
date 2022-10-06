n = int(input())
m = list(map(int,input().split()))
k = []
for i in m:
    if i%2==0:
        k.append(i)
z = len(m)
if len(k)==z:
    print('True')
else:
    print('False')