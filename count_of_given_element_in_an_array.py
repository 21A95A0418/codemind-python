n = int(input())
m = list(map(int,input().split()))
x = int(input())
count = 0
for i in range(0,n):
    if m[i]==x:
        count += 1
print(count)