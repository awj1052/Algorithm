# inDegree가 0인 SCC가 유일하다면 그 노드들을 오름차순으로 출력

import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**6)

# TARJAN
def dfs(cur):
  global id
  id+=1
  d[cur]=id
  stack.append(cur)

  parent=d[cur]
  for e in adj[cur]:
    if not d[e]:
      parent=min(parent,dfs(e))
    elif not finish[e]:
      parent=min(parent,d[e])

  if parent==d[cur]:
    g=[]
    while 1:
      x=stack.pop()
      finish[x]=1
      node[x]=len(css)+1
      g.append(x)
      if x==cur: break
    css.append(sorted(g))
    
  return parent

tc=int(r())
for i in range(tc): # TC
  n,m=map(int,r().split())
  adj=[[] for i in range(n)]
  for i in range(m):
    a,b=map(int,r().split())
    adj[a].append(b)
  r()
    
  node=[0]*n
  d=[0]*n
  finish=[0]*n
  id=0
  stack=[]
  css=[]
  for i in range(n):
    if d[i]: continue
    dfs(i)

  inDegree=[0]*len(css)
  flag=len(css)
  for i in range(n):
    for e in adj[i]:
      if inDegree[node[e]-1]: continue
      if node[i]==node[e]: continue
      inDegree[node[e]-1]=1
      flag-=1
  if flag==1:
    for i in range(len(css)):
      if inDegree[i]: continue
      print(*css[i], sep='\n')
      break
    print()
  else:
    print("Confused\n")
    
    
    
