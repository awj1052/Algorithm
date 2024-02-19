# DFS+BFS+MST

import sys
r=sys.stdin.readline
from collections import deque

# Input
def isOut(y,x):
  return y>=n or y<0 or x<0 or x>=m

dx=[0,0,1,-1]
dy=[1,-1,0,0]
n,m=map(int,r().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,r().split())))

# BFS
def findLand(a,b,c):
  q=deque([(a,b)])
  graph[a][b]=c
  while q:
    y,x=q.popleft()
    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x
      if isOut(ny,nx): continue
      if graph[ny][nx] != 1: continue
      graph[ny][nx] = c
      q.append((ny,nx))

lands=2
for i in range(n):
  for j in range(m):
    if graph[i][j] != 1: continue
    findLand(i,j,lands)
    lands+=1

# DFS
line=[]
def dfs(y,x,k,l,w):
  ny = y + dy[k]
  nx = x + dx[k]
  if isOut(ny,nx): return
  if graph[ny][nx] == l: return
  if graph[ny][nx] == 0:
    dfs(ny,nx,k,l,w+1)
    return
  if w<2: return
  line.append((l-2,graph[ny][nx]-2,w))

for i in range(n):
  for j in range(m):
    if not graph[i][j]: continue
    for k in range(4):
      dfs(i,j,k,graph[i][j],0)

# MST
# 섬 c-2 개
parent=[i for i in range(lands-2)]

def find(x):
  if parent[x]==x:
    return x
  parent[x]=find(parent[x])
  return parent[x]

def merge(x,y):
  x=find(x)
  y=find(y)
  if x>y: parent[x]=y
  else: parent[y]=x

def isUnion(x,y):
  x=find(x)
  y=find(y)
  if x==y: return True
  return False

line.sort(key=lambda x : x[2])

ans=0
for a,b,c in line:
  if isUnion(a,b): continue
  merge(a,b)
  ans+=c

 # 모든 섬이 연결 안되면 -1
parent[0]=find(parent[0])
for i in range(1,lands-2):
  if parent[0]!=find(parent[i]):
    print(-1)
    exit()
print(ans)
  
