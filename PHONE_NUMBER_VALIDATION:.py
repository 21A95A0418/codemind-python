n = int(input())
m = list(str(n))
for i in m:
    if int(i)!=0:
        if len(m)==10:
            print('Valid')
            break
        else:
            print('Invalid')
            break
    else:
        print('Invalid')
        break