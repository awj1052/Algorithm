import sys; r=sys.stdin.readline
T=int(r())
for _ in range(T):
    n=int(r())
    sticker = [list(map(int,r().split())) for _ in range(2)]
    dp = [[0]*(n+2) for _ in range(2)]
    for i in range(n):
        dp[0][i+2] = max(dp[1][i+1], dp[0][i], dp[1][i]) + sticker[0][i]
        dp[1][i+2] = max(dp[0][i+1], dp[0][i], dp[1][i]) + sticker[1][i]
    print(max(dp[0][n+1],dp[1][n+1]))
