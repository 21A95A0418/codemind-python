s = input()
n = []
for i in(s.split()):
    n.append(i)
k = len(n)
m = []
for j in range(1,k+1):
    m.append(n[-j])
print(*(m))