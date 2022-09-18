n = int(input())
m = str(n)
s1 = 0
s = 1
s2 =0
for i in m:
    s1 = int(i)
    s2 += s1**s
    s +=1
if n==s2:
    print('True')
else:
    print('False')