# BOJ 4948
def is_PrimeNum(n): # 에라토스테네스의 체
    if n%2==0:
        if n == 2:
            return 1
        return 0
    end = int(n**(1/2))
    for i in range(3, end+1, 2):
        if n%i==0:
            return 0
    if n==1:
        return 0
    return 1

while True:
   N=int(input())
   if N==0:
      break
   ans=0
   for i in range(N+1,2*N+1):
      if is_PrimeNum(i):
         ans+=1
   print(ans)
   