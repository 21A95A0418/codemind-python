n = int(input())
m = list(map(int,input().split()))
w = n//2
k = []
k1 = []
for i in m:
    if i<=w:
        k.append(i)
    else:
        k1.append(i)
print(sum(k))
print(sum(k1))
            
            
        
    
    