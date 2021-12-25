# 1:100^a 이면 int(pi*(10**a)) 번 충돌함
# (충돌 횟수)*arctan(1/N) < pi
# N=1일 때 arctan(1) = pi/4, 4*arctan(1) = pi 와 같이
# pi보다 작아야함을 보장하기 위해 0.001을 뺌 (1<=N<=500 은 오차X)

# from math import *
# print(int(pi/atan(1/int(input())) - 0.001))

N=int(input())**2
ans=0
A=0;B=-100
while 1:
    if 0<=A<=B: break
    ans+=1
    a = (1-N)/(1+N)*A + 2*N/(1+N)*B
    B = (N-1)/(N+1)*B + 2/(N+1)*A
    A = a
    if A < 0:
        ans+=1
        A*=-1
print(ans)
