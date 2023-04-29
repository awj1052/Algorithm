# 위상정렬 + DP

import sys
r=sys.stdin.readline
from collections import deque

for _ in range(int(r())): # tc
  n,k=map(int,r().split())
  d = [0] + list(map(int,r().split()))
  dp = [0]*(n+1)
  
  l=[[] for i in range(n+1)]
  inDegree = [0]*(n+1)
  for i in range(k):
    x,y=map(int,r().split())
    l[x].append(y)
    inDegree[y]+=1

  w=int(r())

  
  q=deque([])
  for i in range(1,n+1):
    if inDegree[i]: continue
    q.append(i)
    dp[i]=d[i] # DP

  for i in range(n):
    x=q.popleft()
    if x==w:
      print(dp[w])
      break
    for e in l[x]:
      inDegree[e]-=1
      dp[e] = max(dp[e], dp[x]+d[e]) # DP
      if inDegree[e]: continue
      q.append(e)
