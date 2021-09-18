# BOJ 2579
import sys
N=int(sys.stdin.readline())
stair=[]
dp=[0]*N
for _ in range(N):
    stair.append(int(sys.stdin.readline()))
try:
    dp[0]=stair[0]
    dp[1]=dp[0]+stair[1]
    dp[2]=max(stair[0], stair[1])+stair[2]
    for i in range(3,N):
        dp[i]=max(dp[i-3]+stair[i-1], dp[i-2])+stair[i]
except:
    pass
print(dp[N-1])