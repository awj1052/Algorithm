import sys
r=sys.stdin.readline

N, M, K = map(int,r().split())
damage=[]
for _ in range(N):
    damage.append(int(r()))
boss=[]
for _ in range(K):
    P, Q = map(int,r().split())
    boss.append((P,Q))

damage.sort(reverse=1)

def maxMeso(d):
    dp = [0]*901
    for p, q in boss:
        t = (p+d-1)//d
        if 900 < t: continue
        for j in range(900, 0, -1):
            if j-t >= 0 and dp[j-t] != 0:
                dp[j] = max(dp[j], dp[j-t]+q)
        dp[t] = max(dp[t], q)
    return max(dp)

ans=0
for i in range(M):
    ans+=maxMeso(damage[i])
print(ans)
