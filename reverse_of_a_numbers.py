n = int(input())
string =  str(n)
s = ''
k = []
for i in string:
    k.append(i)
k.reverse()
for j in k:
    s += j
print(int(s))