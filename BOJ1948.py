# 위상정렬

import sys
from collections import deque
r=sys.stdin.readline

n=int(r())
m=int(r())

graph=[[] for _ in range(n+1)]
inDegree=[0]*(n+1)
d=[0]*(n+1)
for _ in range(m):
    a,b,c=map(int,r().split())
    graph[a].append((b,c))
    inDegree[b]+=1

s, e = map(int,r().split())
q=deque([s])
rev = [[] for _ in range(n+1)]
for i in range(1,n+1):
    u = q.popleft()
    
    if u==e:
        break
    
    for v, w in graph[u]:
        inDegree[v]-=1

        if d[v] < d[u] + w:
            d[v] = d[u] + w
            rev[v] = [u]
            
        elif d[v] == d[u] + w:
            rev[v].append(u)
            
        if inDegree[v]: continue
        q.append(v)
visit=[0]*(n+1)
q=deque([e])
visit[e]=1
ans=0
while q:
    v = q.popleft()
    
    ans+=len(rev[v])
    
    for u in rev[v]:
        if visit[u]: continue
        visit[u]=1
        q.append(u)
    
print(d[e])
print(ans)
    
