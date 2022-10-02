x = int(input())
y = str(abs(x))
y = y[::-1]
if x<0:
    r = int(y)
    r = r*(-1)
    print(r)
else:
    print(int(y))