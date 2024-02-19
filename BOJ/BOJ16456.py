# BOJ 16456

N=int(input())
if N<=3:
    if N==1:
        print(1)
    elif N==2:
        print(1)
    elif N==3:
        print(2)   
    exit(0)
dp=[0 for _ in range(N+1)]
dp[1]=1
dp[2]=1
dp[3]=2
for i in range(4,N+1):
    dp[i]=(dp[i-1]+dp[i-3])%1000000009
print(dp[N])