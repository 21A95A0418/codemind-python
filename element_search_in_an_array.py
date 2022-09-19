n = int(input())
arr = list(map(int,input().strip().split()))[:n]
a = int(input())
for i in range(len(arr)):
    if arr[i]==a:
        print('True')
        break
if arr[i]!=a:
    print('False')