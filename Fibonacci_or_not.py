def headache(h):
    a,b = 0,1
    if a==h or b==h:
        return True
    c = a+b
    while True:
        if c==h:
            return True
        if c>h:
            return False
        a = b
        b = c
        c = a+b
h = int(input())
res = headache(h)
print(res)
