num = int(input())
sum = 0
temp = 0
if 0<=num<=9:
    print(num)
else:
    if num>0:
        while num!=0:
            r = num%10
            sum += r
            num = num//10
            if  num==0 and sum>9:
                num = sum
                sum = 0
                continue
            if num ==0 and 0<sum<=9:
                print(sum)