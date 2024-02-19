# 처음엔 BFS로 할라했는데 TLE 나와서 벽 부수고 이동하기 참고해서 O(NMN) 으로 했다.
# 파이썬으로 하면 뭔가 2로 나누면서 해도 잘 될 것 같았지만..
# 그냥 어려웠다..

import sys
r=sys.stdin.readline

n,m=map(int,r().split())

graph=[]
for i in range(n):
 graph.append(list(map(int,r().split())))

for i in range(m):
  if graph[0][i]==2:
    graph[0][i]=0
    loc=i

# dp[n][m][k]
dp=[[[0]*n for _ in range(m)] for _ in range(n)]
dp[0][loc][0]=1

for y in range(1,n):
    for x in range(m):
        if graph[y][x]: continue # 현재 위치 못
        if graph[y-1][x]: continue # 머리 위 못
        for k in range(n):
            if x!=m-1 and dp[y-1][x+1][k] and graph[y][x+1]: # 우상 공 && 우 못
                dp[y][x][k+1]+=dp[y-1][x+1][k]
            if x!=0 and dp[y-1][x-1][k] and graph[y][x-1]: # 좌상 공 && 좌 못
                dp[y][x][k+1]+=dp[y-1][x-1][k]
            if dp[y-1][x][k]: # 그냥 떨어짐
                dp[y][x][k]+=dp[y-1][x][k]

for x in range(m):
  for k in range(n-1,0,-1):
    dp[n-1][x][k-1]+=dp[n-1][x][k]//2
    dp[n-1][x][k]%=2

v=[i for i in range(m)]
last=-1
for k in range(n):
  isExist = 0
  w=0
  while w<len(v):
    x=v[w]
    if dp[n-1][x][k]: 
      if not isExist:
        isExist=1
        last=x
        v=v[w:]
        w=0
    elif isExist:
        v.pop(w)
        w-=1
    w+=1

print(last)
