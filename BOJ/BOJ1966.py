# BOJ 1966
from collections import deque
T=int(input())
for _ in range(T):
    N, M = map(int, input().split())
    value=deque(list(map(int, input().split())))
    idx=deque([i for i in range(N)])
    
    cnt=0
    while 1:
        if value[0]==max(value):
            cnt+=1
            if idx[0]==M:
                print(cnt)
                break
            else:
                value.popleft()
                idx.popleft()
        else:
            value.append(value.popleft())
            idx.append(idx.popleft())
