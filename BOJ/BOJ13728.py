# BOJ 13728

# n*n 행렬 M의 행렬식 Dn (n) 은 cofactor로 구하면 Dn-1 + Dn-2 와 같음
# 피보나치 수열처럼 생각하고,
# gcd(a%p, b%p) = gcd(a,b)%p 가 보장될 수 없어 피보나치 gcd에 대해 알아봤다.
# https://www.cut-the-knot.org/arithmetic/algebra/FibonacciMatrix.shtml#nice
# 선형대수 A=[(0,1),(1,1)] A^k = SΛ^(k)S^(-1) 을 통해
# A^(m+n) = A^m * A^n 을 정리하면 f(m+n) = fmf(n+1) + f(m-1)fn 이 유도됨
# f(m+n) 과 gcd와 유클리드 호제법을 통해 피보나치 수열의 gcd를 간단하게 구할 수 있음
# gcd(fi, fj) = gcd(f(i-j),j) 임을 알 수 있고 계속 줄여나가면 gcd(fi, fj) = f(gcd(i,j))

# 수열 {Dn} 은 1 2 3 5 8 .. 이고
# 피보나치 수열은 1 1 2 3 5 .. 이므로 이 차이도 고려해야 함
N=int(input())
if N == 1: print(1);exit()
def gcd(a,b):
    if(b>a): a,b=b,a
    while True:
        r = a%b
        if r == 0: return b
        a = b
        b = r
MOD=10**9+7
D=[1]*(N+1)
D[2]=2
for i in range(3, N+1):
    D[i]=(D[i-1]+D[i-2])%MOD
S=0
for i in range(1,N+1):
    S +=D[gcd(i+1,N+1)-1]
    S %= MOD
print(S)
