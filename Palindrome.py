number = int(input())
list1 = []
list2 = list(str(number))
while number !=0:
    last = number%10
    list1.append(str(last))
    number = number//10
if list1==list2:
    print('True')
else:
    print('False')