n = int(input())
m = n
while True:
    a = str(m)
    b = a[::-1]
    m += int(b)
    d = str(m)
    e = d[::-1]
    if d == e:
        print(int(d))
        break
    