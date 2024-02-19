# BOJ 2206

import sys
from collections import deque
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dfs():
    loop = deque([(0,0,0)])
    while loop:
        a,b,f = loop.popleft()
        if a==N-1 and b==M-1:
            return visit[a][b][f]
        for i in range(4):
            da=a+dx[i]
            db=b+dy[i]
            if 0<=da<N and 0<=db<M and visit[da][db][f]==0:
                if v[da][db] == '0':
                    loop.append((da,db,f))
                    visit[da][db][f]=visit[a][b][f]+1
                elif f==0:
                    loop.append((da,db,1))
                    visit[da][db][1]=visit[a][b][0]+1
    return -1

N,M = map(int,input().split())
v=[]
visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
visit[0][0][0]=1
for _ in range(N):
    v.append(list(input().rstrip()))
print(dfs())