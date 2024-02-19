# BOJ 20002
import sys
N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
sum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    tmp = sys.stdin.readline().split()
    for j in range(N):
        arr[i][j] = int(tmp[j])

for i in range(N):
    for j in range(N):
        sum[i+1][j+1] = sum[i+1][j] + sum[i][j+1] - sum[i][j] + arr[i][j]

cost = -1000

for y in range(N):
    for x in range(N):
        r=1
        while x+r <= N and y+r <= N:
            cost = max(cost,sum[y+r][x+r]-sum[y][x+r]-sum[y+r][x]+sum[y][x])
            r+=1
print(cost)