n = int(input())
m = list(map(int,input().split()))
a,b = map(int,input().split())
l = []
for i in m:
    if i<a or i>b:
        l.append(i)
if len(l)>0:
	print(max(l))
else:
	print("-1")