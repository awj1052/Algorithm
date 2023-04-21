# Sort + MST
# 터널 길이가 min(dx, dy, dz) 이므로 x,y,z 각각에 대해 정렬하는게 포인트

import sys
r=sys.stdin.readline

# Input
n=int(r())
planet=[]
for i in range(n):
  a,b,c=map(int,r().split())
  planet.append((a,b,c,i))

# Sort
graph=[]
for i in range(3):
  l=sorted(planet, key=lambda x : x[i])
  for j in range(n-1):
    graph.append((l[j][3],l[j+1][3],l[j+1][i]-l[j][i]))

# MST
parent=[i for i in range(n)]

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

graph.sort(key=lambda x : x[2])

ans=0
for a,b,c in graph:
  if isUnion(a,b): continue
  merge(a,b)
  ans+=c
print(ans)
