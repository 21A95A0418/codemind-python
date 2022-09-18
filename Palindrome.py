n = int(input())
m = str(n)
s = int(m[::-1])
if n==s:
    print('True')
else:
    print('False')