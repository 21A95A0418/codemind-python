a = int(input())
b = list(map(int,input().split()))
for i in range(max(b),0,-1):
    s = 0
    for j in b:
        if j%i==0:
            s+=1
    if s==a:
        print(i)
        break
    else:
        s=0
        
            