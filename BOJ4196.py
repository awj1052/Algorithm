# 코사라주 알고리즘 -> 각 SCC의 inDegree 설정 -> inDegree가 0인 SCC 개수 출력

import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs1(cur):
  global cntnum
  visit[cur]=1
  for a in adj[cur]:
    if visit[a]: continue
    dfs1(a)
  nums[cur]=cntnum
  cntnum+=1

def dfs2(cur):
  stack.append(cur)
  visit[cur]=1
  for a in revAdj[cur]:
    if visit[a]: continue
    dfs2(a)

for _ in range(int(r())): # TC
  v,e=map(int,r().split())
  adj=[[] for i in range(v+1)]
  revAdj=[[] for i in range(v+1)]
  
  for i in range(e):
    a,b=map(int,r().split())
    adj[a].append(b)
    revAdj[b].append(a)
  
  nums = [0]*(v+1)
  visit=[0]*(v+1)
  cntnum=1
  
  for i in range(1,v+1):
    if nums[i]: continue
    dfs1(i)
  
  liter=list(enumerate(nums))
  liter.sort(key=lambda x : -x[1])
  
  stack=[]
  visit=[0]*(v+1)
  css=[0]*(v+1)
  cssCnt=0
  for i,_ in liter:
    if i==0: continue
    if visit[i]: continue
    dfs2(i)
    
    cssCnt+=1
    while stack:
      x=stack.pop()
      css[x]=cssCnt
  inDegree=[0]*(cssCnt+1)
  ans=cssCnt
  for i in range(1,v+1):
    for j in adj[i]:
      if css[i] == css[j]: continue
      if inDegree[css[j]]: continue
      inDegree[css[j]]=1
      ans-=1
  print(ans)
