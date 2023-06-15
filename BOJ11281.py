# 2-SAT - 4
# tarjan 알고리즘을 x1, x2, .. , xn, -x1, -x2, ... , -xn 순으로 시행하여
# scc[i] < scc[-i] 이면 scc[-i]->scc[i] 또는 둘이 이어지지 않아서 xi를 True로 해도 True->False가 존재하지 않음 (아마도)

import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**5)

# TARJAN
id=0
stack=[]
def dfs(u):
    global id, sccCnt
    id+=1
    d[u]=id
    stack.append(u)
    
    parent=d[u]
    for v in graph[u]:
        if d[v]==0:
            parent = min(parent, dfs(v))
        elif not finish[v]:
            parent = min(parent, d[v])
    
    if parent==d[u]:
        sccCnt+=1
        while stack:
            e=stack.pop()
            finish[e]=1
            scc[e]=sccCnt
            if u==e: break
    
    return parent
    

n,m=map(int,r().split())
graph=[[] for _ in range(2*n+1)]
d=[0]*(2*n+1)
finish=[0]*(2*n+1)
scc=[0]*(2*n+1)
sccCnt=0
for _ in range(m):
    a,b=map(int,r().split())
    
    graph[-a].append(b)
    graph[-b].append(a)

for i in range(1,2*n+1):
    if d[i]: continue
    dfs(i)
    
result=[0]*n
for i in range(1,n+1):
    if scc[i]==scc[-i]:
        print(0)
        break
    if scc[i] < scc[-i]:
        result[i-1]=1
else:
    print(1)
    print(*result)
