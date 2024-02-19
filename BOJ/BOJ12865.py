# BOJ 12865
import sys
N,K = map(int, sys.stdin.readline().split())
dp=[0 for _ in range(K+1)]
for i in range(N):
    w,v=map(int, sys.stdin.readline().split())
    if w > K:
        continue
    for j in range(K, 0, -1):
        if j-w >= 0 and dp[j-w] != 0:
            dp[j]=max(dp[j], dp[j-w]+v)
    dp[w]=max(dp[w], v)
print(max(dp))