# SCC, 2-SAT

import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**5)

# TARJAN

id=0
def dfs(u):
    global id, css
    id+=1
    d[u]=id
    stack.append(u)
    
    parent = d[u]
    for v in graph[u]:
        if d[v]==0:
            parent=min(parent, dfs(v))
        elif not finish[v]:
            parent=min(parent, d[v])
    
    if parent==d[u]:
        css+=1
        while stack:
            e=stack.pop()
            finish[e]=1
            group[e]=css
            if e==u: break
    return parent
    

n,m=map(int,r().split())

d = [0]*(2*n+1)
finish = [0]*(2*n+1)
group = [0]*(2*n+1)
graph=[[] for _ in range(2*n+1)]
for _ in range(m):
    a,b=map(int,r().split())
    
    if a>0:
        not_a = 2*a-1
        a = 2*a
    else:
        not_a = 2*(-a)
        a = 2*(-a)-1
        
    if b>0:
        not_b = 2*b-1
        b = 2*b
    else:
        not_b = 2*(-b)
        b = 2*(-b)-1
        
    graph[not_a].append(b)
    graph[not_b].append(a)
        
css=0
stack=[]
for i in range(1, 2*n+1):
    if d[i]: continue
    dfs(i)

for i in range(1,n+1):
    if group[i*2]==group[i*2-1]:
        print(0)
        break
else:
    print(1)
