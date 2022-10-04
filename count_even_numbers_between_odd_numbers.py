n = int(input())
m = list(map(int,input().split()))
s = 0
i = 1
while i<(n-1):
    if m[i-1]%2!=0 and m[i+1]%2!=0 and m[i]%2==0:
        s+=1
    i += 1
print(s)