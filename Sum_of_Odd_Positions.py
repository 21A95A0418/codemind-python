n = int(input())
m = list(map(int,input().strip().split()))
x = 0
for i in range(len(m)):
    if i%2!=0:
        x += m[i]
print(x)