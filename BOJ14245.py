# 16975처럼 레이지 안써도 풀림
# a^0 = a

import sys, math
r=sys.stdin.readline

def init(node, s, e):
    if s==e:
        tree[node] = arr[s]
        return
    m=(s+e)//2
    init(node*2, s, m)
    init(node*2+1, m+1, e)
    
def update(node, s, e, l, r, c):
    if r < s or e < l:
        return
    if l <= s and e <= r:
        tree[node] ^= c
        return
    m=(s+e)//2
    update(node*2, s, m, l, r, c)
    update(node*2+1, m+1, e, l, r, c)
    
def query(node, s, e, idx, ans):
    if idx < s or e < idx:
        return 0
    ans ^= tree[node]
    if s==e:
        return ans
    m=(s+e)//2
    lq = query(node*2, s, m, idx, ans)
    rq = query(node*2+1, m+1, e, idx, ans)
    return lq^rq

n=int(r())
arr=list(map(int,r().split()))

tree = [0] * (1<<(math.ceil(math.log2(n))+1))

init(1, 0, n-1)

m=int(r())
for _ in range(m):
    cmd=list(map(int,r().split()))
    
    if cmd[0]==1: # 1 a b c
        update(1, 0, n-1, cmd[1], cmd[2], cmd[3])
    
    else: # 2 a
        print(query(1, 0, n-1, cmd[1], 0))
