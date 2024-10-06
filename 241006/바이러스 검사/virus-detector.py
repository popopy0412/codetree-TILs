n=int(input())
l=[*map(int,input().split())]
a,b=map(int,input().split())
ans=n
for i in l:
    if i-a < 0: continue
    ans+=(i-a)//b + (1 if (i-a)%b else 0)
print(ans)