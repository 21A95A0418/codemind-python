n = input()
m = n[::-1]
a = []
b = []
for i in n.split():
    for j in i:
        a.append(ord(j))
    b.append(chr(min(a)))
    a.clear()
    break
for k in m.split():
    for o in k:
        a.append(ord(o))
    b.append(chr(max(a)))
    break
print(*b)