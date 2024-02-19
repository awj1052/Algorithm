import sys
r=sys.stdin.readline
 
n=int(r())
for _ in range(n):
    sl = r().rstrip()
    a=0
    b=0
    for e in sl:
        if e == "A":
            a+=1
        else:
            b+=1
    print("A" if a>b else "B")