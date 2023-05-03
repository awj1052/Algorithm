# 이전꺼는 타잔 알고리즘(Tarjan's Algorithm
# 코사라주 알고리즘(Kosaraju's Algorithm)

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

# Main
ans=[]
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
for i, v in liter:
  if i==0: continue
  if visit[i]: continue
  dfs2(i)

  css=[]
  while stack:
    x=stack.pop()
    css.append(x)
  ans.append(sorted(css))

print(len(ans))
for e in sorted(ans):
  print(*e,-1)
