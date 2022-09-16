n = int(input())
lst = list(map(int,str(n)))
for i in range(len(lst)):
    if lst[i]==6:
        lst[i] = 9
        break
for j in lst:
    print(j,end = '')