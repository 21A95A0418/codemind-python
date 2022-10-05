a=int(input())
b=list(map(int,input().split()))
s=[]
m=0
for i in range(1,(a-1)):
    if (b[i-1]%2==0 and b[i+1]%2!=0) or (b[i-1]%2!=0 and b[i+1]%2==0):
        s.append(b[i])
if (b[-2]%2!=0 and b[0]%2==0) or (b[-2]%2==0 and b[0]%2!=0):
    m+=1
if (b[-1]%2!=0 and b[1]%2==0) or (b[-1]%2==0 and b[1]%2!=0):
    m+=1
k=len(s)
print(k+m)