# BOJ 16496
import sys
from functools import cmp_to_key
def compare(a,b): # 
    if len(a) < len(b):
        c=list(map(int, a))
        d=list(map(int, b))
        swap=0
    else:
        c=list(map(int, b))
        d=list(map(int, a))
        swap=1
    for i in range(len(c)):
        if c[i] < d[i]:
            return -1 if swap else 1
        elif c[i] > d[i]:
            return 1 if swap else -1
    for i in range(len(c), len(d)):
        if c[0] < d[i]:
            return -1 if swap else 1
        elif c[0] > d[i]:
            return 1 if swap else -1
    return 0

N=int(sys.stdin.readline())
num=sys.stdin.readline().split()
num.sort(key=cmp_to_key(compare))
if num[0]=='0':
    print(0)
else:
    print(*num, sep='')
