# BOJ 2170
import sys
input=sys.stdin.readline
N=int(input())
lines=[]
for _ in range(N):
    a,b=map(int,input().split())
    lines.append((a,b))

lines.sort(key=lambda x : (x[1], -x[0]), reverse=True)

ans=0
last=lines[0][1]
for fr, to in lines:
    if fr <= last:
        if to < last:
            last=to
        ans+=last-fr
        last=fr
print(ans)