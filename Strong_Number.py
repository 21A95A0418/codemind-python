n = int(input())
a = n
s =0
p = 1
while n:
    r = n%10
    while r:
        p *= r
        r -= 1
    s = s+p
    p=1
    n //= 10
if s ==a:
    print('The number',a,'is a strong number')
else:
    print('The number',a,'is not a strong number')
    