import sys
r=sys.stdin.readline
from collections import deque

n, m= map(int,r().split())
graph=[["."]*m for i in range(n)]
iry, irx = 0,0
iby, ibx = 0,0
for i in range(n):
  tmp = list(r())
  for j in range(m):
    if tmp[j]=="R":
      iry=i; irx=j
    elif tmp[j]=="B":
      iby=i; ibx=j
    else:
      graph[i][j]=tmp[j]

dx = [0,0,-1,1]
dy=  [-1,1,0,0]

def main():

  q=deque([(iry,irx,iby,ibx,0,1,-1)])
  
  while q:

    ify,ifx,ily,ilx,it,cnt,pre=q.popleft() # BFS

    for i in range(4):
      if pre==i: continue # 이전과 같은 움직임 배제
        
      fy,fx, ly,lx = ify,ifx, ily,ilx
      t=it
      
      flag=0 # 좌표 비교 후 어떤 구슬 먼저 움직일지
      if i==0: # 상
        if fx == lx and fy > ly:
          flag=1          
      elif i==1: # 하
        if fx == lx and fy < ly:
          flag=1
      elif i==2: # 좌
        if fx > lx and fy == ly:
          flag=1
      else: # 우 
        if fx < lx and fy == ly:
          flag=1

      if flag: # t가 0이면 F가 빨강, t가 1이면 L이 빨강
        t=(t+1)%2
        fy,ly=ly,fy
        fx,lx=lx,fx

      # f 움직임
      ok=0
      cflag=0
      for x1 in range(9):
        b = graph[fy + dy[i]][fx + dx[i]]
        if b=="#":
          break
        if b=="O":
          if t==0: # 빨강이면
            ok=1 # 파란 구슬도 빠지는지 확인해야함
            fy=-1; fx=-1 # 구슬이 빠져나감
            break
          cflag=1 # 파란 구슬이 빠지면 진행 X
          break
        fy += dy[i]
        fx += dx[i]

      if cflag:
        continue

      # l 움직임 : f 움직임 + a
      cflag=0
      for x2 in range(9):
        b = graph[ly + dy[i]][lx + dx[i]]
        if b=="#":
          break
        if ly+dy[i]==fy and lx+dx[i]==fx: # F 충돌 확인
          break
        if b=="O":
          if t==1: # 빨강이면
            print(cnt)
            return
          cflag=1 # 파랑이면 진행 X
          break
        ly += dy[i]
        lx += dx[i]

      if cflag:
          continue
      if ok: # 빨강이 빠졋고 파랑도 안빠지면 출력
        print(cnt)
        return

      if cnt+1>10: continue # 10번만 움직여봄  
      q.append((fy,fx,ly,lx,t,cnt+1,i))
      
  print(-1) # 10번보다 크거나 답 없음

main() 
