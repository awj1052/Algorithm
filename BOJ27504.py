# KMP
# 처음엔 KMP 함수에서 j==0 일때마다 x=T[i]-패턴[0]을 설정하고 비교했는데 반례가 있는듯
# K_i, L >= 2 이므로 a_i, b_i의 차이를 활용함

import sys
r=sys.stdin.readline

def KMP(T):
  P=nb
  #table = makeTable(P)
  j=0
  for i in range(len(T)):
    while j>0 and T[i]!=P[j]:
      j=table[j-1]
    if T[i]==P[j]:
      if j==len(P)-1:
        return True
      else:
        j+=1
  return False

def makeTable(P):
  #table = [0 for i in range(len(P))]

  j=0
  for i in range(1,len(P)):
    while j>0 and P[i]!=P[j]:
      j=table[j-1]
    if P[i]==P[j]:
      j+=1
      table[i]=j

  return table

n=int(r())
song=[]
for i in range(n):
  l,*a=map(int,r().split())
  na=[0 for i in range(l-1)]
  for j in range(l-1):
    na[j]=a[j]-a[j+1]
  song.append(na)

l=int(r()) # L
b=list(map(int,r().split()))
nb=[0 for i in range(l-1)]
for i in range(l-1):
  nb[i]=b[i]-b[i+1]

table = [0 for i in range(len(nb))]
makeTable(nb)

flag=False
for i in range(n):
  if KMP(song[i]):
    flag=True
    print(i+1, end=' ')
if not flag:
  print(-1)
