# BOJ 14719
import sys
r=sys.stdin.readline
H,W = map(int, r().split())
num=list(map(int, r().split()))
high_idx=0
for i in range(1, W):
    if num[high_idx] < num[i]:
        high_idx=i

ans=0
high=0
for i in range(0,high_idx):
    if high < num[i]:
        high=num[i]
    else:
        ans+=high-num[i]
high=0
for i in range(W-1, high_idx, -1):
    if high < num[i]:
        high=num[i]
    else:
        ans+=high-num[i]
print(ans)