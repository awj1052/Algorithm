# BOJ 16457

def clear():
     cnt=0
     for q in quest:
          flag=1
          for s in q:
               if s in key:
                    flag=0
                    break
          if flag:
               cnt+=1
     return cnt

def dfs(a, b):
     global answer
     if b>n:
          answer=max(answer,clear())
          return
     for i in range(a,2*n+1):
          if check[i] == 0:
               check[i]=1
               key[b]=i
               dfs(i+1, b+1)
               check[i]=0

import sys
n,m,k=[int(i) for i in sys.stdin.readline().split()]
key=[0 for _ in range(n+1)]
check=[0 for _ in range(2*n+1)]
answer=0
quest=[]
for _ in range(m):
     quest.append([int(i) for i in sys.stdin.readline().split()])
dfs(1, 1)
print(answer)