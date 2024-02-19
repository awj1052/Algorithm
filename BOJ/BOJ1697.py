# BOJ 1697
from collections import deque
N,K=[int(i) for i in input().split()]
q=deque([N])
MAX = 100000
num=[0 for _ in range(MAX+1)]
while q:
     x=q.popleft()
     if x==K:
          print(num[K])
          exit(0)
     if x-1>=0 and num[x-1]==0:
          q.append(x-1)
          num[x-1]=num[x]+1
     if x+1 <= MAX and num[x+1]==0:
          q.append(x+1)
          num[x+1]=num[x]+1
     if x*2 <= MAX and num[x*2]==0:
          q.append(x*2)
          num[x*2]=num[x]+1

