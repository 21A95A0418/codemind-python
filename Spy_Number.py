n = str(input())
n = list(n)
s = 0
s1 = 1
for i in n:
    s += int(i)
for j in n:
    s1 *= int(j)
if s==s1:
    print('Spy Number')
else:
    print('Not Spy Number')