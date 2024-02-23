import sys
r=sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
H,W=map(int,r().split())
R,C,D=map(int,r().split())

dust = [[1]*W for _ in range(H)]
visit = [[[0]*4 for _ in range(W)] for _ in range(H)]

A=[]
for _ in range(H):
    A.append(list(map(int,list(r().rstrip()))))

B=[]
for _ in range(H):
    B.append(list(map(int,list(r().rstrip()))))

ans=dummy=clear=0
while 1:
    
    if dust[R][C]:
        dust[R][C] = 0
        D = (D + A[R][C])%4
        clear+=1
        dummy=0
    else:
        D = (D + B[R][C])%4
        if visit[R][C][D] == clear:
            break
        visit[R][C][D] = clear
        dummy+=1
    
    R += dy[D]
    C += dx[D]
    ans+=1
    if not (0 <= R < H) or not (0 <= C < W):
        break

print(ans-dummy)
