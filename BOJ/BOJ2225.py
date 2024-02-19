# BOJ 2225

def comb(m, n):
   if n==0 or n==m or m==1:
          return 1
   if n==1 or n==m-1:
      return m%1000000000
   if c[m][n]==0:
      c[m][n]=(comb(m-1, n-1)+comb(m-1, n))%1000000000
   return c[m][n]

N,K=[int(i) for i in input().split()]
c=[[0 for _ in range(N+1)] for _ in range(N+K)]
print(comb(N+K-1,N))
