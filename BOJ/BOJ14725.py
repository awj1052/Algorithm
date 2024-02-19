# Trie, Sort, DFS

class Node:
  def __init__(self,key):
    self.key=key
    self.children = {}

class Trie:
  def __init__(self):
    self.head=Node(None)

  def insert(self,st):
    cur = self.head

    for s in st:
      if s not in cur.children:
        cur.children[s] = Node(s)
      cur = cur.children[s]        

import sys
r=sys.stdin.readline

trie=Trie()

n=int(r())
for i in range(n):
  k,*t=r().split()
  trie.insert(t)

def dfs(cur,d):
  for s in sorted(cur.children):
    print('--'*d, s, sep='')
    dfs(cur.children[s],d+1)

dfs(trie.head, 0)
  
