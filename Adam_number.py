a = int(input())
b = a**2
c = list(str(b))
d = []
r = 0
r1 =0
for i in c:
    d.append(i)
while a!=0:
    digit = a%10
    r = r*10+digit
    a //= 10
e = r**2
while e!=0:
    digit = e%10
    r1 = r1*10+digit
    e //= 10
f = list(str(r1))
if d==f:
    print("True")
else:
    print('False')