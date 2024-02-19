# (1) i번째 비행기를 G_i번째 게이트에 넣음
# (2) 그 게이트가 차있으면 -1 을 한 게이트에 넣음
# (3) 넣을 때까지 (2)를 반복함 [그리디]. 단, 0까지 가면 폐쇄

# (2)를 구현할 때 Union-Find를 사용

import sys
r=sys.stdin.readline

def find(x):
  if parent[x]==x:
    return x
  parent[x]=find(parent[x])
  return parent[x]

def merge(x,y):
  x=find(x)
  y=find(y)
  if x==y: return False
  if x>y: parent[x]=y
  else: parent[y]=x
  return True

parent=[]
def main():
  global parent
  G=int(r())
  P=int(r())
  parent=[i for i in range(G+1)]

  ans=0
  for _ in range(P):
    i=int(r())
    if find(i)==0: return ans
    merge(i, find(i)-1)
    ans+=1
  return ans
  
print(main())
