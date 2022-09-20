n = int(input())
lst = list(str(n))
a = 1
b = 0
for i in lst:
    a *= int(i)
for j in lst:
    b += int(j)
print(a-b)