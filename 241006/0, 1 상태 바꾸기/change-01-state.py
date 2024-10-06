n,m=map(int,input().split())
l=[*map(int,input().split())]
for _ in range(m):
    a,b,c=map(int,input().split())
    if a == 1: l[b-1]=c
    elif a == 2:
        for i in range(b-1,c): l[i]^=1
    elif a == 3:
        for i in range(b-1,c): l[i]=0
    else:
        for i in range(b-1,c): l[i]=1
print(*l)