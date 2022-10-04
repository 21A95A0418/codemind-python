for i in range(int(input())):
    a = input()
    b = '0123456789'
    c = 0
    for i in a:
        if i not in b:
            c+= 1
    print(c==0)
            