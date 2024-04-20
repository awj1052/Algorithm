import sys
r=sys.stdin.readline
 
comb = []
for i in range(2,2**5):
    comb.append(int(str(bin(i)).replace("0b", "")))
 
for _ in range(int(r())):
    n = int(r())
    for i in range(len(comb)-1,-1,-1):
        while n%comb[i]==0:
            n //= comb[i]
        if n == 1:
            print("YES")
            break
    else:
        print("NO")