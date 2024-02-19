# BOJ 11051

def comb(m, n):
     if m==1 or n==0 or n==m:
          return 1
     if n==1 or n==m-1:
          return m
     if dp[m][n]==0:
          dp[m][n]=(comb(m-1,n-1)+comb(m-1,n))%10007
     return dp[m][n]

N,K=[int(i) for i in input().split()]
dp=[[0 for _ in range(K+1)] for _ in range(N+1)]
print(comb(N,K))