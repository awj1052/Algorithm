# BOJ 1111

# 직선의 방정식을 생각하고 len이 1,2, 3보다 같거나 클 때로
# 나누면 짜기 쉬운 문제. 골2 급은 아니라 생각함
# 연산 횟수 줄이려고 for문을 3부터,2부터로 했는데 오히려 반례를 만듦.

import sys
r=sys.stdin.readline
l=int(r());n=[int(t) for t in r().split()]
if l>2:
    c1=n[1]-n[0];c2=n[2]-n[1]
    if c1==0:a=1;b=0
    elif (c2)%(c1)!=0:print('B');exit(0)
    else:a=(c2)//(c1);b=n[1]-n[0]*a
    for i in range(l-1):
        if n[i+1]!=n[i]*a+b:print('B');exit(0)
    print(n[-1]*a+b)
elif l==2:
    if n[0]==n[1]:print(n[0])
    else:print('A')
else:print('A')