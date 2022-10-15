x = int(input())
y = list(map(int,input().split()))
w = []
z = []
a = []
h = []
for i in y:
    if i%2==0:w.append(i)
    else:z.append(i)
if len(w)>len(z):maxi = w
else:maxi = z
l = min(len(w),len(z))
for j in range(0,l):
    a.append(w[j])
    a.append(z[j])
a = a+maxi[l:]
if x%2==0:
    print(*a)
else:
    a.append(0)
    print(*a)