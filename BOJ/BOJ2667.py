# BOJ 2667
import sys
from collections import deque
input=sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs():
    loop.append((0,0))
    while loop:
        a,b=loop.popleft()
        for i in range(4):
            da=a+dx[i]
            db=b+dy[i]
            if 0<=da<N and 0<=db<N:
                if v[db][da]==0:
                    loop.append((da,db))
                    v[db][da]=-1
                elif v[db][da]==1:
                    v[db][da]=len(r)+2
                    r.append(1)
                    dfs(da,db)

def dfs(a,b):
    for i in range(4):
        da=a+dx[i]
        db=b+dy[i]
        if 0<=da<N and 0<=db<N:
            if v[db][da]==0:
                loop.append((da,db)) 
            if v[db][da]==1:
                v[db][da] = v[b][a]
                r[v[b][a]-2]+=1
                dfs(da,db)                

N=int(input())
v=[]
r=[]
loop = deque([])
for _ in range(N):
    v.append(list(map(int, list(input().rstrip()))))
bfs()
r.sort()

print(len(r), *r, sep='\n')
