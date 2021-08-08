import sys
from collections import deque
queue=deque()
M, N = [int(i) for i in sys.stdin.readline().split()] # bfs
graph = [[0 for _ in range(N)] for _ in range(M)] # [M][N]
for i in range(N):
    tmp = sys.stdin.readline().split()
    for j in range(M):
        if tmp[j] == "1":
            queue.append([j,i])
        graph[j][i] = int(tmp[j])
cnt=-1
while queue:
    cnt+=1
    for _ in range(len(queue)):
        m, n = queue.popleft()
        for i in range(4):
            if i == 0: # UP
                if m+1 < M and n < N:
                    if graph[m+1][n] == 0:
                        graph[m+1][n]=1
                        queue.append([m+1,n])
            elif i == 1: # LEFT
                if m < M and n-1 >= 0:
                    if graph[m][n-1] == 0:
                        graph[m][n-1]=1
                        queue.append([m,n-1])
            elif i == 2: # RIGHT
                if m < M and n+1 < N:
                    if graph[m][n+1] == 0:
                        graph[m][n+1]=1
                        queue.append([m,n+1])
            elif i == 3: # DOWN
                if m-1 >= 0 and n < N:
                    if graph[m-1][n] == 0:
                        graph[m-1][n]=1
                        queue.append([m-1,n])
for a in graph:
    if 0 in a:
        print(-1)
        exit(0)
print(cnt)