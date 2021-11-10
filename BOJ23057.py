# BOJ 23057
# https://wtg-study.tistory.com/98

import sys
N=int(sys.stdin.readline())
v=[]
m=0
for i in sys.stdin.readline().split():
    v.append(int(i))
    m+=int(i)
s=set()

# 백트래킹
def dfs(idx, sum):
    s.add(sum)
    if idx==N:
        return
    dfs(idx+1, sum+v[idx])
    dfs(idx+1, sum)

dfs(0, 0)
print(m-len(s)+1)

# 비트마스크
# select=1
# while True:
#     if select == (1 << N):
#         break
#     sum=0
#     for i in range(N):
#         if select & (1 << i):
#             sum+=v[i]
#     s.add(sum)
#     select+=1
# print(m-len(s))

# set 합집합
# for i in map(int, input().split()):
#   S = S | {s+i for s in S}  # S |= {s+i for s in S}
#   m+=i