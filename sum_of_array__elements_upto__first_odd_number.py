n = int(input())
m = list(map(int,input().split()))
s = []
for i in m:
    if i%2!=0:
        break
    else:
        s.append(i)
print(sum(s))