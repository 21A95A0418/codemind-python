t = int(input())
for _ in range(t):
    a = int(input())
    b = list(map(int,input().split()))
    c = sorted(b)
    if b==c:
        print(0)
    else:
        p=min(b)
        q=max(b)
        print(q-p)