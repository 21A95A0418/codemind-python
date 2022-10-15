a = int(input())
b = list(map(int,input().split()))
k = []
for i in b:
    if i % 2!=0:
        if i not in k:
            k.append(i)
print(sum(k))