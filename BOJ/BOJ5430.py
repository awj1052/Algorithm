# BOJ 5430
import sys
from collections import deque
T=int(sys.stdin.readline())
for _ in range(T):
     cmd = sys.stdin.readline().rstrip()
     n=int(sys.stdin.readline())
     tmp=sys.stdin.readline().rstrip()[1:-1]
     if n==0:
          data=deque([])
     else:
          data=deque(tmp.split(","))
     r=False
     flag=True
     for c in cmd:
          if c=='R':
               r = not r
          elif c=='D':
               if len(data) != 0:
                    if r:
                         data.pop()
                    else:
                         data.popleft()
               else:
                    flag=False
                    print('error')
                    break
     if flag:
          if r:
               data.reverse()
               print('[' + ','.join(data) + ']')
          else:
               print('[' + ','.join(data) + ']')
