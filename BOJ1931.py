# BOJ 1931
import sys
r=sys.stdin.readline
time=sorted([list(map(int, r().split())) for _ in range(int(r()))], key=lambda x : (x[1], x[0]))
ans = fin = 0
for start, end in time:
    if start >= fin:
        fin=end
        ans+=1
print(ans)