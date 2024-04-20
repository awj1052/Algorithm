import sys
r=sys.stdin.readline
 
for _ in range(int(r())):
    t=int(r())
    for i in range(2*t):
        for j in range(2*t):
            if ((i//2)%2==0 and (j//2)%2==0) or ((i//2)%2==1 and (j//2)%2==1):
                print("#",end='')
            else:
                print(".",end='')
        print()