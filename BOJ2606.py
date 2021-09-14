# BOJ 2606
import sys
from collections import deque
C=int(sys.stdin.readline())
graph = [[0 for _ in range(C+1)] for _ in range(C+1)]
for _ in range(int(sys.stdin.readline())):
     m,n=map(int, sys.stdin.readline().split())
     graph[m][n]=1
     graph[n][m]=1
q = deque([1])
virus=[1]
cnt=0
while q:
     c = q.popleft()
     for i in range(1,C+1):
          if graph[c][i] and i not in virus:
               q.append(i)
               virus.append(i)
print(len(virus)-1)
