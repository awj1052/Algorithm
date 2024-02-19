# BOJ 1011
T=int(input())
for _ in range(T):
     a,b=map(int, input().split())
     i=0
     while 1:
          if i*(i-1) < b-a <= i**2:
               print(i*2-1)
               break
          if i**2 < b-a <= i*(i+1):
               print(i*2)
               break
          i+=1