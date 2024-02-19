# 단절점 Articulation Point

import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**4)

id=0
ans=[]
def dfs(u, isRoot):
    global id, lenP
    id+=1
    d[u]=id
    
    child=0
    parent = d[u]
    for v in graph[u]:
        if d[v]==0:
            child+=1
            res = dfs(v, False)
            parent = min(parent, res)
            if not isRoot and res >= d[u]:
                p[u]=1
        else:
            parent = min(parent, d[v])

    if isRoot and child >=2:
        p[u]=1
    return parent
    

v,e=map(int,r().split())
graph=[[] for _ in range(v+1)]
d=[0]*(v+1)
p=[0]*(v+1)
for _ in range(e):
    a,b=map(int,r().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,v+1):
    if d[i]: continue
    dfs(i, True)
    
ans=0
for i in range(1,v+1):
    if p[i]: ans+=1

print(ans)
for i in range(1,v+1):
    if p[i]:
        print(i, end=' ')
