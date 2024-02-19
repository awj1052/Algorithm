# BOJ 2812
N,K=[int(i) for i in input().split()]
M = list(input())
stack=[]
a=K
for i in M:
     while stack and a>0 and stack[-1] < i:
          stack.pop()
          a-=1
     stack.append(i)
print(''.join(stack[:N-K]))