# BOJ 16953
from collections import deque
A,B=map(int, input().split())
q=deque([A])
cnt=0
while q:
     cnt+=1
     for _ in range(len(q)):
          a = q.popleft()
          if a == B:
               print(cnt)
               exit(0)
          if a*2 <= B:
               q.append(a*2)
          if a*10+1 <= B:
               q.append(a*10+1)
print(-1)

# cnt=[0 for _ in range(B+1)] # B <= 10**9 이므로 메모리 초과 남
# cnt[A]=1
# while q:
#      a = q.popleft()
#      if a == B:
#           print(cnt[B])
#           exit(0)
#      if a*2 <= B:
#           q.append(a*2)
#           cnt[a*2] = cnt[a]+1
#      if a*10+1 <= B:
#           q.append(a*10+1)
#           cnt[a*10+1] = cnt[a]+1
# print(-1)
