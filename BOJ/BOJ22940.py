def elimination(A, b):
    N = len(A)
    for i in range(0,N-1):
        for j in range(i+1, N):
            pv = A[j][i]/A[i][i]
            b[j] -= b[i]*pv
            for k in range(i, N):
                A[j][k] -= A[i][k]*pv 
    x = [0]*N
    for i in range(N-1,-1,-1):
        a=0
        for j in range(N-1, i, -1):
            a+=x[j]*A[i][j] 
        x[i] = (b[i]-a)/A[i][i]
    return x
    

import sys; r=sys.stdin.readline
N=int(r())
A=[[0]*N for _ in range(N)]
b=[0]*N
for i in range(N):
    tmp = r().split()
    for j in range(N):
        A[i][j] = float(tmp[j])
    b[i] = float(tmp[N])
x = elimination(A,b)
for ans in x:
    print(round(ans), end=' ')
