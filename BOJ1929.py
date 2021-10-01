# BOJ 1929
# Python 3   29200KB  2124ms
# PyPy 3    127524KB   604ms
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

M,N=map(int,input().split())
for i in range(M,N+1):
    if is_PrimeNum(i):
        print(i)