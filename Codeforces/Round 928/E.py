import sys
r=sys.stdin.readline
 
tc = int(r())
for _ in range(tc):
    n, k = map(int, r().split())
 
    i=0
    last=n
    while k > (last+1)//2 and last:
        k -= (last+1)//2
        last -= (last+1)//2
        i+=1
    
    print((2**i) * (2*k-1))