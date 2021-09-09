# BOJ 14499

import sys

def move(c):
    global x,y
    if c == 1: # E
        if y+1<M:
            y+=1
            dice[3],dice[0],dice[2],dice[5]=dice[0],dice[2],dice[5],dice[3]
            return 1
    elif c == 2: # W
        if y-1>=0:
            y-=1
            dice[3],dice[0],dice[2],dice[5]=dice[5],dice[3],dice[0],dice[2]
            return 1
    elif c == 3: # N
        if x-1>=0:
            x-=1
            dice[1],dice[0],dice[4],dice[5]=dice[5],dice[1],dice[0],dice[4]
            return 1
    elif c == 4: # S
        if x+1<N:
            x+=1
            dice[1],dice[0],dice[4],dice[5]=dice[0],dice[4],dice[5],dice[1]
            return 1
    return 0

N,M,x,y,K=[int(i) for i in sys.stdin.readline().split()]
dice = ['0' for _ in range(6)]
#   1     N  5    E  1 
# 3 0 2    3 1 2   0 2 3
#   4        0       4
#   5        4       5  
maps=[]
for _ in range(N):
    maps.append(sys.stdin.readline().split())
cmd=sys.stdin.readline().split()
for c in cmd:
    if move(int(c)):
        if maps[x][y] == '0':
            maps[x][y] = dice[0]
        else:
            dice[0]=maps[x][y]
            maps[x][y]='0'
        print(dice[5])