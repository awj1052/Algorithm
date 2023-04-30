# 2048 Easy

import sys
r=sys.stdin.readline

n=int(r())
board=[]
for i in range(n):
  board.append(list(map(int,r().split())))

ans=0
def dfs(cnt):
  global ans
  
  if cnt==6:
    for i in range(n):
      for j in range(n):
        ans=max(ans,board[i][j])    
    return
    
  tmp = [[0]*n for i in range(n)]
  for i in range(n):
    for j in range(n):
      tmp[i][j]=board[i][j]
  
  for r in range(4):
    move(r)
    dfs(cnt+1)
    
    for i in range(n):
      for j in range(n):
        board[i][j]=tmp[i][j]

def move(r):
  if r==0: # 상
    for x in range(n):
      t=0
      p=0
      for y in range(n):
        e=board[y][x]
        if e==0: continue
        board[y][x]=0
        if p>0:
          if p==e:
            board[t][x]=p*2
            t+=1
            p=0
          else:
            board[t][x]=p
            t+=1
            p=e
        else:
          p=e
      board[t][x]=p
    
  elif r==1: # 하
    for x in range(n):
      t=n-1
      p=0
      for y in range(n):
        e=board[n-y-1][x]
        if e==0: continue
        board[n-y-1][x]=0
        if p>0:
          if p==e:
            board[t][x]=p*2
            t-=1
            p=0
          else:
            board[t][x]=p
            t-=1
            p=e
        else:
          p=e
      board[t][x]=p
    
  elif r==2: # 좌
    for y in range(n):
      t=0
      p=0
      for x in range(n):
        e=board[y][x]
        if e==0: continue
        board[y][x]=0
        if p>0:
          if p==e:
            board[y][t]=p*2
            t+=1
            p=0
          else:
            board[y][t]=p
            t+=1
            p=e
        else:
          p=e
      board[y][t]=p
      
  else: # 3 우
    for y in range(n):
      t=n-1
      p=0
      for x in range(n):
        e=board[y][n-x-1]
        if e==0: continue
        board[y][n-x-1]=0
        if p>0:
          if p==e:
            board[y][t]=p*2
            t-=1
            p=0
          else:
            board[y][t]=p
            t-=1
            p=e
        else:
          p=e
      board[y][t]=p

dfs(1)
print(ans)
