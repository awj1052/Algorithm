import sys
r=sys.stdin.readline

class Polution:
    def __init__(self, x, p):
        self.x = x
        self.p = p

n = int(r())
a = []
for _ in range(n):
    x, p = map(int,r().split())
    a.append(Polution(x, p))

a.sort(key = lambda e : e.x)

usedCount = 1
bottomUp = a[0].p
for i in range(n-1):
    bottomUp += usedCount * (a[i+1].x - a[i].x) + a[i+1].p
    usedCount += 1

usedCount = 1
topDown = a[n-1].p
for i in range(n-1, 0, -1):
    topDown += usedCount * (a[i].x - a[i-1].x) + a[i-1].p
    usedCount += 1

ans = bottomUp
for i in range(n):
    ans = min(ans, bottomUp - a[i].p - (a[n-1].x - a[i].x))

for i in range(n-1, -1, -1):
    ans = min(ans, topDown - a[i].p - (a[i].x - a[0].x))

ans = min(ans, bottomUp - a[-1].p - (n - 1) * (a[-1].x - a[-2].x))
ans = min(ans, topDown - a[0].p - (n - 1) * (a[1].x - a[0].x))

print(ans)
