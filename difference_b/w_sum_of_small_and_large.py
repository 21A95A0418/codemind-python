x = input()
y = []
z = []
a = []
b = []
for i in x.split():
    for j in i:
        y.append(ord(j))
    z.append(min(y))
    y.clear()
for k in x.split():
    for m in k:
        a.append(ord(m))
    b.append(max(a))
    a.clear()
s = sum(z)
n = sum(b)
print(abs(s-n))