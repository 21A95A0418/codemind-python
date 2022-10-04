a = input()
b = "1234567890"
c = 0
for i in a:
    if i in b:
        c += int(i)
print(c)