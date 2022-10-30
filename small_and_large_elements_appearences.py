n = input()
a =[]
b = []
c=0
d = 0
for i in n.split():
    for j in i:
        a.append(ord(j))
    e = chr(min(a))
    f = chr(max(a))
for i in n:
    if i==e:
        d+=1
    elif i == f:
        c+=1
print(e,d,f,c)
        
    