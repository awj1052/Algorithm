import sys
r=sys.stdin.readline

N, M = map(int, r().split())
S = [0] + list(map(int, r().split()))
A, D = map(int, r().split())

upper = (N+D-1)//D # ceil(N/D)

dp = [[0 for _ in range(N+D)] for _ in range(upper+1)]
for i in range(1,N+1):
    for j in range(upper+1):
        if j != 0 and dp[j][i-1] == 0: continue
        dp[j][i] = max(dp[j][i], dp[j][i-1] + S[i])
        if j != upper:
            dp[j+1][i+D-1] = max(dp[j+1][i+D-1], dp[j][i-1] + A)

for i in range(upper+1):
    if max(dp[i]) >= M:
        print(i)
        break
else:
    print("-1")
