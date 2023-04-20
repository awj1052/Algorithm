# 최소 신장 트리(MST) 기본 문제
# 유니온 파인드 + 정렬 -> MST 

import sys
r=sys.stdin.readline

def find(x):
  if x==parent[x]:
    return x
  parent[x]=find(parent[x])
  return parent[x]

def merge(x,y):
  x=find(x)
  y=find(y)
  if x<y: parent[y]=x
  else: parent[x]=y

def isUnion(x,y):
  x=find(x)
  y=find(y)
  if x==y: return True
  return False

v,e=map(int,r().split())
parent=[i for i in range(v+1)]
graph=[]
for i in range(e):
  a,b,c=map(int,r().split())
  graph.append((a,b,c))

graph.sort(key=lambda x : x[2])

ans=0
for i in range(e):
  a,b,c=graph[i]
  if not isUnion(a,b):
    merge(a,b)
    ans+=c
print(ans)
