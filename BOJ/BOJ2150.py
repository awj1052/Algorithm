# Strongly Connected Component (SCC) 기본 문제
# 오름차순 출력 > Sort

import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

v,e=map(int,r().split())
graph=[[] for i in range(v+1)]
for i in range(e):
  a,b=map(int,r().split())
  graph[a].append(b)

ans=[]

finished=[0]*(v+1)
stack=[]
d=[-1]*(v+1)
id=0
def dfs(cur):
  global id, ans
  id+=1
  d[cur]=id
  stack.append(cur)
  
  parent = d[cur]
  for adj in graph[cur]:
    if d[adj]==-1:
      parent=min(parent, dfs(adj))
    elif not finished[adj]:
      parent=min(parent, d[adj])

  if parent==d[cur]:
    scc=[]
    while 1:
      x = stack.pop()
      finished[x]=1
      scc.append(x)
      if cur==x: break
    ans.append(sorted(scc))
  return parent

for i in range(1,v+1):
  if d[i]==-1: dfs(i)

print(len(ans))
for e in sorted(ans):
  print(*e, -1)
    
