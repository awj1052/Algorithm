# BOJ 18419

def digit(a):
    sum=0
    while a>0:
        sum+=a%10
        a//=10
    return sum

N=int(input())
dp=[0 for _ in range(N+1)]
cnt=1
dp[N]=1
for i in range(N, 0, -1):
    v = i+digit(i)
    if dp[i] == 0 and v<=N and dp[v] == 1:
        cnt+=1
        dp[i]=1
print(cnt)