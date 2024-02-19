# BOJ 5639

def post_order(start, end):
    if start > end:
        return
    div=end+1
    for i in range(start+1, end+1):
        if tree[start] < tree[i]:
            div=i
            break
    post_order(start+1, div-1)
    post_order(div,end)
    print(tree[start])

import sys
sys.setrecursionlimit(10**9)
tree=[]
while 1:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break
post_order(0, len(tree)-1)