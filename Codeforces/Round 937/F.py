import sys, math
r=sys.stdin.readline
 
for _ in range(int(r())):
    a,b,c=map(int,r().split())
 
    if a == 0:
        if c != 1:
            print(-1)
            continue
        print(b)
        continue
 
    h = int(math.log2(a))
    rest = 2**(h+1) - 1 - a
    rest2 = (a - 2**h + 1)*2
    if rest+rest2 != c:
        print(-1)
        continue
    if rest <= b:
        b -= rest
        rest2 += rest
        h += (b+rest2-1)//rest2
    print(h+1)