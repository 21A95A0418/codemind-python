def calculate_hcf(a,b):
    if a>b:
        smaller = b
    else:
        smaller = a
    for i in range(1,smaller+a):
        if ((a%i==0) and (b%i==0)):
            hcf = i
    return hcf
a,b = map(int,input().split())
print(calculate_hcf(a,b))