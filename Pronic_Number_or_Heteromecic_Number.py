n = int(input())
num = 100
s = []
for i in range(1,num):
    num = i*(i+1)
    s.append(num)
if n in s:
    print("YES")
else:
    print('NO')