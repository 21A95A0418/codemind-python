n = int(input())
g = True
k = True
while n!=0:
    r = n%10
    if r%2==0:
        k = False
    else:
        g = False
    n //= 10
if k==False and g==True:
    print('Even')
elif k==True and g==False:
    print('Odd')
else:
    print('Mixed')
        