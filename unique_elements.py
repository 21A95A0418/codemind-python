
z = int(input())
x = list(map(int,input().split()))
k = []
for i in x:
    if i not in k:
        k.append(i)
print(*(k))