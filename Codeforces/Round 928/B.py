import sys
r=sys.stdin.readline
 
tc=int(r())
for _ in range(tc):
    n=int(r())
    
    graph = []
    for i in range(n):
        graph.append(list(r().rstrip()))
    
    flag=0
    sX, sY, width, height = -1, -1, 0, 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "1":
                if sX + sY < 0:
                    sY = i
                    sX = j
                    for y in range(i+1, n):
                        if graph[y][j] == "0": break
                        height+=1
                    for x in range(j+1, n):
                        if graph[i][x] == "0": break
                        width+=1
                else:
                    if not (sY <= i <= sY+height): flag=-1
                    if not (sX <= j <= sX+width): flag=-1
    if flag == 0:
        flag = 1
    print("SQUARE" if flag==1 else "TRIANGLE")