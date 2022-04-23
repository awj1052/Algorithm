# https://github.com/Leewongi0731/DailyCodeTest/blob/main/%5B%EB%B0%B1%EC%A4%80%20%ED%94%8C%EB%A0%885%5D%2020415%EB%B2%88.py

def num(rank):
    if rank == "B": return 0
    elif rank== "S": return 1
    elif rank == "G": return 2
    elif rank == "P": return 3
    return 4
n=int(input())
p=[0] +  list(map(int,input().split()))
p+=[200000]
r = list(map(num,list(input())))
dp=[0]*n
if r[0]==4: dp[0]=p[4]
else: dp[0]=p[r[0]+1]-1
for i in range(1,n):
    if r[i] == 4:
        dp[i]=p[4]; continue
    if dp[i-1]+dp[i]<p[r[i]+1]-1:
        dp[i]=p[r[i]+1]-dp[i-1]-1
    elif dp[i-1]+dp[i]>p[r[i]+1]-1:
        dp[i]=0
        dp[i-1]=p[r[i]+1]-1
        for j in range(i-1,0,-1):
            if dp[j-1]+dp[j]<p[r[j]]:
                dp[j-1]=p[r[j]]-dp[j]
            elif dp[j-1]+dp[j]>p[r[j]+1]-1:
                dp[j-1]=p[r[j]+1]-dp[j]-1
            else: break
print(sum(dp))
