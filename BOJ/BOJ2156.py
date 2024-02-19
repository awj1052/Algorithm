# BOJ 2156
import sys
n=int(sys.stdin.readline())
podo=[]
for _ in range(n):
    podo.append(int(sys.stdin.readline()))
dp=[0]*n
try:
    dp[0]=podo[0]
    dp[1]=podo[0]+podo[1]
    for i in range(2,n+1):
        dp[i] = max(dp[i-1], dp[i-3]+podo[i-1]+podo[i], dp[i-2]+podo[i])
except:
    pass
print(dp[n-1])