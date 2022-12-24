number  = int(input())
dup1 = str(number)
k1 = []
for i in dup1:
    prime1 = 0
    org = int(i)
    for j in range(1,org+1):
        if org%j==0:
            prime1 +=1 
    if prime1 == 2:
        k1.append(org)
prime2 = 0
for k in range(1,number+1):
    if number%k==0:
        prime2+=1
if len(k1)== len(dup1) and prime2 == 2:
    print('Mega Prime')
else:
    print('Not Mega Prime')
