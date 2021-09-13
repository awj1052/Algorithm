# BOJ 2178
import sys
from collections import deque
N,M = map(int, sys.stdin.readline().split())
maze = []
for i in range(N):
     maze.append(list(sys.stdin.readline()))
visit=[[0 for _ in range(M)] for _ in range(N)]
visit[0][0] = 1
q=deque([[0,0]])
dx=[-1,1,0,0]
dy=[0,0,-1,1]
while q:
     y, x = q.popleft()
     if y == N-1 and x == M-1:
          print(visit[y][x])
          break
     for i in range(4):
          nx=x+dx[i]
          ny=y+dy[i]
          if 0 <= nx < M and 0 <= ny < N and maze[ny][nx]=='1' and visit[ny][nx]==0:
               visit[ny][nx] = visit[y][x] + 1
               q.append([ny,nx])