n = int(input())
m = list(map(int,input().split()))
a,b = map(int,input().split())
s = []
for i in m:
    if i<a or i>b:
        s.append(i)
print(sum(s))