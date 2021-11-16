# BOJ 10026

import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
N=int(input())
rgb=[[]*N for _ in range(N)]
for i in range(N):
    rgb[i]=list(input().rstrip())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(a,b):
    visit[a][b]=1
    for i in range(4):
        da=a+dx[i]   
        db=b+dy[i]
        if 0<=da<N and 0<=db<N and rgb[da][db]==rgb[a][b] and not visit[da][db]:
            dfs(da,db)

# 적록색약이 아닌 사람이 봤을 때의 구역의 개수
visit=[[0]*N for _ in range(N)]
cnt=0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            cnt+=1
            dfs(i,j)
print(cnt, end=' ')

# 적록색약인 사람이 봤을 때의 구역의 개수
visit=[[0]*N for _ in range(N)]
cnt=0
for i in range(N):
    for j in range(N):
        if rgb[i][j]=='G':
            rgb[i][j]='R'

for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            cnt+=1
            dfs(i,j)
print(cnt)