# 단절점/단절선
# https://www.geeksforgeeks.org/bridge-in-a-graph/
# SCC 타잔 알고리즘 변형
# 재밌는듯..

import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**6)

v,e=map(int,r().split())
adj=[[] for i in range(v+1)]
for _ in range(e):
    a,b=map(int,r().split())
    adj[a].append(b)
    adj[b].append(a)
    
d=[0]*(v+1)
ans=[]
id=0
def dfs(u, pre):
    global id
    id+=1
    d[u]=id
    
    parent=d[u]
    for v in adj[u]:
        if d[v]==0:
            res=dfs(v, u)
            parent=min(parent, res)
            if res > d[u]:
                ans.append((u,v) if u<v else (v,u))
            
        elif v != pre:
            parent=min(parent, d[v])

    return parent

for i in range(1,v+1):
    if d[i]: continue
    dfs(i,-1)

print(len(ans))
for e in sorted(ans):
    print(*e)
