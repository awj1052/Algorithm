# 세그먼트 트리
# https://book.acmicpc.net/ds/segment-tree

import sys, math
r=sys.stdin.readline
mod=10**9+7

def init(a, tree, node, start, end):
    if start==end:
        tree[node]=a[start]
        return
    init(a, tree, node*2, start, (start+end)//2)
    init(a, tree, node*2+1, (start+end)//2+1, end)
    tree[node] = tree[node*2] * tree[node*2+1] % mod
    
def update(a, tree, node, start, end, index, val):
    if index > end or index < start:
        return
    if start==end:
        a[index]=val
        tree[node]=val
        return
    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2] * tree[node*2+1] % mod
    
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum * rsum % mod
    
n,m,k=map(int,r().split())
a=[int(r()) for _ in range(n)]

tree_height = math.ceil(math.log2(n))
tree = [1]*(1<<(tree_height+1))
init(a, tree, 1, 0, n-1)

for _ in range(m+k):
    w,b,c=map(int,r().split())
    
    if w==1: # update
        update(a, tree, 1, 0, n-1, b-1, c)
    else: # w==2; print
        q = query(tree, 1, 0, n-1, b-1, c-1)
        print(q)
