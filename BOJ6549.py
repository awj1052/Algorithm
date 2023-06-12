# 세그먼트 트리 (Pypy3)
# 어렵다 ..

import sys, math
r=sys.stdin.readline
sys.setrecursionlimit(10**5)

NMAX=10**9
def init(tree, a, node, s, e):
    if s==e:
        tree[node]=s
        return
    m=(s+e)//2
    init(tree, a, node*2, s, m)
    init(tree, a, node*2+1, m+1, e)
    if a[tree[node*2]] < a[tree[node*2+1]]:
        tree[node]=tree[node*2]
    else:
        tree[node]=tree[node*2+1]
    
def findMin(tree, a, node, s, e, l, r):
    if r < s or l > e:
        return -1
    if s >= l and r >= e:
        return tree[node]
    m=(s+e)//2
    idxL = findMin(tree, a, node*2, s, m, l, r)
    idxR = findMin(tree, a, node*2+1, m+1, e, l, r)
    
    if idxL == -1:
        return idxR
    if idxR == -1:
        return idxL
    if a[idxL] < a[idxR]:
        return idxL
    return idxR
    
def query(tree, a, s, e):
    if s==e:
        return a[s]
    
    idxA = findMin(tree, a, 1, 0, len(a)-1, s, e)
    
    a1=a2=0
    if idxA-1 >= s:
        a1 = query(tree, a, s, idxA-1)
    if idxA+1 <= e:
        a2 = query(tree, a, idxA+1, e)
    
    return max(a[idxA]*(e-s+1), a1, a2)
    
def main():
    
    while 1:
        n,*a=map(int,r().split())
        if n==0:
            return
        
        tree=[0]*(1<<(math.ceil(math.log2(n))+1))
        
        init(tree, a, 1, 0, n-1)
        print(query(tree, a, 0, n-1))
        
main()
