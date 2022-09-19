def prime(n):
    a = n**0.5
    for i in range(2,int(a)+1):
        if n%i==0:
            return False
    return True
n = int(input())
m =  int(input())
count = 0
for j in range(n,m+1):
    if j <=1:
        continue
    if prime(j):
        count += 1
print(count)