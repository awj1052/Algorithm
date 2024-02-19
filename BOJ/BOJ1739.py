# (A and D) or (B and C) == (A or B) and (A or C) and (D or B) and (D or C)

import sys
r=sys.stdin.readline

def tarjan(u):
    global id, sccCnt
    id+=1
    d[u]=id
    stack.append(u)
    
    parent = d[u]
    for v in graph[u]:
        if d[v]==0:
            parent = min(parent, tarjan(v))
        elif not finish[v]:
            parent = min(parent, d[v])
    
    if parent == d[u]:
        sccCnt+=1
        while stack:
            top = stack.pop()
            finish[top]=1
            scc[top]=sccCnt
            if top == u: break
    
    return parent
    
tc = int(r())
for _ in range(tc):
    n,m,k=map(int,r().split())
    graph = [[] for _ in range((n+m)*2+1)]
    
    for _ in range(k):
        a,b,c,d=map(int,r().split())
        
        if a==c and b==d:
            continue
        
        b+=n; d+=n # line numbering
        if b<d:
            aa,cc=a,c
        else:
            aa,cc=-a,-c
        if a<c:
            bb,dd=b,d
        else:
            bb,dd=-b,-d

        graph[-aa].append(cc)
        graph[-cc].append(aa)
        
        graph[-aa].append(bb)
        graph[-bb].append(aa)
        
        graph[-dd].append(cc)
        graph[-cc].append(dd)
        
        graph[-dd].append(bb)
        graph[-bb].append(dd)
            
    d = [0]*((n+m)*2+1)
    finish = [0]*((n+m)*2+1)
    stack=[]
    id=0
    sccCnt=0
    scc = [0]*((n+m)*2+1)
    for i in range(1,(n+m)*2+1):
        if d[i]: continue
        tarjan(i)
    
    for i in range(1, (n+m)+1):
        if scc[i] == scc[-i]:
            print("No")
            break
    else:
        print("Yes")
        
