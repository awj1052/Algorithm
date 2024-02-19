# BOJ 3117 YouTube

import sys
r=sys.stdin.readline

n,k,m=map(int,r().split())
student=list(map(int,r().split()))
next_video=list(map(int,r().split()))
m-=1
p=0
while 2**p < m:
  p+=1
p+=1

sparse_table = [[0]*p for i in range(k+1)]
for i in range(k):
  sparse_table[i+1][0]=next_video[i]

for i in range(1,p):
  for j in range(1,k+1):
    sparse_table[j][i]=sparse_table[sparse_table[j][i-1]][i-1]

  
div_m=[]
for i in range(p):
  if (1<<i)&m:
    div_m.append(i)
  
for s in student:
  ans=s
  for d in div_m:
    ans=sparse_table[s][d]
  print(ans,end=' ')
