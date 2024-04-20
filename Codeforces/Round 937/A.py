import sys
r=sys.stdin.readline
 
for _ in range(int(r())):
    a,b,c=map(int,r().split())
    if a<b<c:
        print("STAIR")
    elif a<b>c:
        print("PEAK")
    else:
        print("NONE")