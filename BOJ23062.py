# BOJ 23062
# A,B,C 소인수분해에서 시간이 오래걸려 더 알아봐야 함

class nums:
    def __init__(self):
        self.a = []
        self.y = []
        self.A=0
        self.Y=0

def gcd(a,b): # 최대공약수
    if b==0:
        return a
    return gcd(b,a%b)

def Factorization(num, flag=0): # 인수분해
    dic=defaultdict(int)
    if flag:
        for p in prime:
            while p<=num and num%p==0:
                dic[p]+=1
                num//=p
        if num != 1:
            dic[num]+=1
        return dic
    else:
        while 2<=num:
            if num%2==0:
                dic[2]+=1
                num//=2
            else:
                break
        d=3
        while d<=num:
            if num%d==0:
                dic[d]+=1
                num//=d
            else:
                d+=2
        return dic

def mul_inv(a,b): # 역원
    if b==1:
        return 1
    b0=b
    x0,x1=0,1
    while a > 1:
        q = a // b
        a,b = b,a%b
        x0,x1=x1-q*x0,x0
    if x1 < 0:
        x1+=b0
    return x1

def check(): # 해 존재 여부 판정, 모든 M값 곱
    global M
    for root in eq.keys():
        for i in range(len(eq[root].a)):
            if eq[root].Y%(root**eq[root].a[i]) != eq[root].y[i]: # 해 존재 여부 판정
                return False 
        M*=root**eq[root].A 
    return True

import sys
from collections import defaultdict
T=int(sys.stdin.readline())

for _ in range(T): # x%A=a, x%B=b, x%C=c
    num=list(map(int, sys.stdin.readline().split()))

    # A,B,C 각 쌍의 최대공약수를 소인수분해하여 A,B,C를 다시 소인수분해함
    prime=set()
    for key in Factorization(gcd(num[0],num[1])).keys():
        prime.add(key)
    for key in Factorization(gcd(num[1],num[2])).keys():
        prime.add(key)
    for key in Factorization(gcd(num[2],num[0])).keys():
        prime.add(key)

    eq = defaultdict(nums)
    for i in range(3):
        F = Factorization(num[i],1)
        for root in F.keys(): # coin = y (mod a)
            eq[root].y.append(num[i+3]%(root**F[root])) # 나머지
            eq[root].a.append(F[root]) # 지수
            if eq[root].A < F[root]:
                eq[root].A = F[root]
                eq[root].Y = num[i+3]%(root**F[root])

    M=1
    if not check():
        print(-1)
        continue
    coin=0 # 금화 개수의 최소값 
    for root in eq.keys():
        if eq[root].Y == 0:
            continue
        m = M//(root**eq[root].A)
        n = mul_inv(m, root**eq[root].A)
        coin+=n*m*eq[root].Y
    print(coin%M)