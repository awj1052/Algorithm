import sys
r=sys.stdin.readline
 
def sumof(i):
    res=0
    while i:
        res+=i%10
        i//=10
    return res
 
dp=[0]*(200001)
for i in range(200001):
    dp[i] = dp[i-1] + sumof(i)
 
tc = int(r())
for _ in range(tc):
    n = int(r())
    print(dp[n])