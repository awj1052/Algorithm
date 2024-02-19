# 이분탐색, 매개변수 탐색
# hi를 처음엔10**10 으로 잡아서 WA
# m이 10**12보다 작거나 같으니 10**12보단 커야해서 10**13으로 함

import sys
r=sys.stdin.readline

n,m=map(int,r().split())
l=list(map(int,r().split()))
a=list(map(int,r().split()))

maxLv=0
lv=[]
for i in range(n):
  maxLv=max(maxLv,l[i])
  lv.append(int(((4*l[i]*(l[i]-1)+8*a[i]+1)**.5+1)//2))

def reqPotion(mid):
  req=0
  for i in range(n):
    req+=max(0,mid-lv[i])
  return req   

lo=0
hi=10**13
while lo+1<hi:
  mid=(lo+hi)//2
  if reqPotion(mid) <= m:
    lo=mid
  else:
    hi=mid
print(lo if lo>=maxLv else -1)
