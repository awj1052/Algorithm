# HACKED

import sys
r=sys.stdin.readline
 
def getFactor(n):
    res = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            res.append(i) 
            if ( (i**2) != n) : 
                res.append(n // i)
    res.sort()
    return res
 
# n를 소인수분해
# 나눠서 비교했는데 1 아니면 나눈 만큼-1 차이나면 ok
 
for _ in range(int(r())):
    n = int(r())
    s = list(r().rstrip())
    factors = getFactor(n)
    for f in factors:
        ss = set()
        loc = set()
        cnt = 0
        for i in range(n//f-1):
            for k in range(f):
                if s[k] != s[(i+1)*f+k]:
                    ss.add((s[(i+1)*f+k], k))
                    cnt += 1
        if cnt == 0 or cnt == 1 or (cnt==n//f-1 and len(ss)==1):
            print(f)
            break