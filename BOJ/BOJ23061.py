# BOJ 23061 PyPy3
class item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

if __name__ != "__main__":
    exit(0)

import sys
N,M = map(int, sys.stdin.readline().split())
m=[]
for i in range(N):
    w,v = map(int, sys.stdin.readline().split())
    m.append(item(w,v))
bag=[]
bag_max=0
for i in range(M):
    bag.append(int(sys.stdin.readline()))
    bag_max=max(bag_max,bag[i])
dp=[0]*(bag_max+1)
for j in range(N):
    if m[j].weight > bag_max:
        continue
    for k in range(bag_max, 0, -1):
        if k-m[j].weight >= 0:
            dp[k]=max(dp[k], dp[k-m[j].weight] + m[j].value)
e=0
idx=0
for i in range(M):
    if e < dp[bag[i]]/bag[i]:
        e=dp[bag[i]]/bag[i]
        idx=i
print(idx+1)