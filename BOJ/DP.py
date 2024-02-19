#https://www.acmicpc.net/problem/1003
a0 = [0 for _ in range(41)]
a1 = [0 for _ in range(41)]
def fib(N, n): # TOP-DOWN
    if a0[N] != 0:
        return a0[N], a1[N]
    elif n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        if a0[n] == 0:
            a,b = fib(N, n-1)
            c,d = fib(N, n-2)
            a0[n] = a+c
            a1[n] = b+d
        return a0[n], a1[n]
a0[0] = 1 # DOWN-UP
#a1[0] = 0
#a0[1] = 0
a1[1] = 1
last_pos=1
def fib2(N):
    global last_pos
    if a0[N] == 0:
        for i in range(last_pos+1, N+1):
            a0[i] = a0[i-1] + a0[i-2]
            a1[i] = a1[i-1] + a1[i-2]
        last_pos = N
    return a0[N], a1[N]

for _ in range(int(input())):
    t = int(input())
    a,b = fib2(t) # a,b = fib(t,t)
    print(a,b)