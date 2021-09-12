# BOJ 1520
import sys
sys.setrecursionlimit(10000)
def dfs(m,n):
     if m==M-1 and n==N-1:
          return 1
     if num[m][n]!=-1:
          return num[m][n]
     num[m][n]=0
     if m-1>=0 and maps[m][n]>maps[m-1][n]: # DOWN
          num[m][n]+=dfs(m-1,n)
     if n+1<N and maps[m][n]>maps[m][n+1]: # RIGHT
          num[m][n]+=dfs(m,n+1)
     if n-1>=0 and maps[m][n]>maps[m][n-1]: # LEFT
          num[m][n]+=dfs(m,n-1)
     if m+1<M and maps[m][n]>maps[m+1][n]: # UP
          num[m][n]+=dfs(m+1,n)
     return num[m][n]


M,N = [int(i) for i in sys.stdin.readline().split()] # 세로 가로
maps=[]
num=[[-1 for _ in range(N)] for _ in range(M)] # num[세로][가로]
for _ in range(M):
     maps.append([int(i) for i in sys.stdin.readline().split()]) # maps[세로][가로]
print(dfs(0,0))

