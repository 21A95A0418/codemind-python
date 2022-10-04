n = int(input())
m = list(map(int,input().strip().split()))
k = 0
x = []
for i in range(len(m)):
    k += m[i]
    x.append(m[i])
    
s = k//(len(m))
if s in x:
    print('True')
else:
    print('False')