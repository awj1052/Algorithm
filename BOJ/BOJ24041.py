def getG(time):
    res=[]
    g=0;k=0
    for i in range(N):
        if O[i]: # O가 1인 것만 따로 정렬
            res.append(S[i]*max(1, time-L[i]))
        else:
            g += S[i]*max(1, time-L[i])
    res.sort(reverse=True)
    for r in res:
        if k<K:
            k+=1
        else:
            g+=r
    return g    

import sys; r=sys.stdin.readline
N,G,K = map(int,r().split())
S=[];L=[];O=[]
for _ in range(N):
    s,l,o=map(int,r().split())
    S.append(s);L.append(l);O.append(o)
start=0
end=2*(10**9) # 답의 최대는 N=1, G=1e9, S=1, L=1e9 일 때 2e9
# https://www.acmicpc.net/blog/view/109 반영한 코드
while start + 1 < end:
    mid = (start + end) // 2
    g = getG(mid)
    if g <= G: start = mid # 이분탐색 잘못 짜서 고생했다
    else: end = mid
print(start)
