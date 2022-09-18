n = int(input())
i = 1
while(i*i)<=n:
    k = i*i
    if n==k:
        print('True')
        break
    i += 1
if n!=k:
    print('False')