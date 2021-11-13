# BOJ 18194
# permutation 으로 모든 경우의 수 stack으로 했으나 메모리 초과
# n마리의 소 중 i번째 소보다 키가 작은 소의 마리 수 k라 할 때 
# i번째 소가 확인할 수 있는 마리 수 기댓값 k / (n-k+1)
# QX + C(-k) = 1 의 X를 확장 유클리드 호제법으로 구하고 P 곱셈
# gcd(Q, C) = 1 이므로 X가 유일하게 존재함 (C=10**9+7, C는 소수)
# X == x0 + n(C/g) (mod C) , g=gcd(Q, C)=1 이므로 X=x0

import sys

def exeu(a, b):
    r = [a, b] 
    s = [1, 0] 
    t = [0, 1] 
    while r[-1] != 0: 
        q = int(r[-2] / r[-1]) 
        r.append(r[-2] - q * r[-1]) 
        s.append(s[-2] - q * s[-1]) 
        t.append(t[-2] - q * t[-1]) 
    return s[-2]

C = 10**9 + 7
input=sys.stdin.readline
n=int(input())
cow=list(map(int,input().split()))
cow.sort()

tmp=cow[0]
ans=0
num=0
for i in range(1,n):
    if cow[i] != tmp:
        num=i
        tmp=cow[i]
    ans+=exeu(n-num+1, C)*num%C
    ans%=C
print(ans)