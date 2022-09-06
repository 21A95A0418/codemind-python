num = int(input())
s = 0
n = num**2
n = list(str(n))
#print(n)
for i in n:
    s += int(i)
n=int(num)
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')