# BOJ 10974
def dfs(n):
    if n==N:
        print(' '.join(map(str, num)))
        return
    for i in range(1, N+1):
        if not visit[i]:
            visit[i]=True
            num[n]=i
            dfs(n+1)
            visit[i]=False

N=int(input())
visit=[False for _ in range(N+1)]
num=[0 for _ in range(N)]
dfs(0)