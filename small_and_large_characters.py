n = input()
a =[]
b = []
c = []
d = []
for i in n.split():
    for j in i:
        a.append(ord(j))
    c = min(a)
    d = max(a)
    b.append(chr(c))
    b.append(chr(d))
    a.clear()
print(*b)