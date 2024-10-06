n=int(input())
l=[*map(int,input().split())]
a,b=map(int,input().split())
ans=n
for i in l:
    ans+=(i-a)//b + 1 if (i-a)%b else 0
print(ans)