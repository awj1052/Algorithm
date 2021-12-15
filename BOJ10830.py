import sys; r=sys.stdin.readline

def multi_matrix(a,b): # N*N N*N 행렬 곱셈
    res=[[0]*N for _ in range(N)]
    for i in range(0,N):
        for l in range(0,N):
            for j in range(0, N):
                res[i][l]+=(a[i][j]*b[j][l])%1000
            res[i][l]%=1000
    return res

N,B=map(int,r().split())
A=[list(map(int,r().split())) for _ in range(N)]
res=[[0]*N for _ in range(N)]
for i in range(N):
    res[i][i]=1
while B > 0: # 분할정복
    if B%2==1:
        res=multi_matrix(res,A)
    A=multi_matrix(A,A)
    B//=2
for a in res:
    for b in a:
        print(b, end=' ')
    print()
