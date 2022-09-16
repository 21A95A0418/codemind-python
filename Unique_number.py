a = int(input())
b = str(a)
k = []
for i in b:
    k.append(i)
c = len(k)
p = list(dict.fromkeys(k))
d = len(p)
if c==d:
    print('Unique Number')
else:
    print('Not Unique Number')