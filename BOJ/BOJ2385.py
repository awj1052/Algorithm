# BOJ 2385

# m 값을 찾는 중 # a+'0'+b, b+'0'+a 비교했더니 오답
# a+zero[0]+b, b+zero[0]+a 비교했더니 정답
# ex) a=530, zero[0]=004, b=53005

import sys
from functools import cmp_to_key
def compare(a,b):
    return int(a+b)-int(b+a)
r=sys.stdin.readline
r()
num=[]
zero=[]
for n in r().split():
    if n[0] != '0':
        num.append(n)
    else:
        zero.append(n)
num.sort(key=cmp_to_key(compare))
zero.sort(key=cmp_to_key(compare))
if len(num) == 0:
    print('INVALID')
else:
    m = 0
    if zero:
        for i in range(len(num)):
            if int(num[m]+zero[0]+num[i]) > int(num[i]+zero[0]+num[m]):
                m=i
    print(num[m], end='')
    print(*zero,sep='',end='')
    for i in range(0,m):
        print(num[i], end='')
    for i in range(m+1, len(num)):
        print(num[i], end='')
print()