n = input()
a = []
b = []
for i in n.split():
    for j in i:
        a.append(ord(j))
    c = max(a)
    d = min(a)
    b.append(abs(d-c))
    a.clear()
print(*b)