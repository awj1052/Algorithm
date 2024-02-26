n = int(input())
a = list(map(int,input().split()))

ai = dict()
mv=0
for e in a:
    if e in ai.keys():
        ai[e] += 1
    else:
        ai[e] = 1
    if ai[e] > mv:
        mv = ai[e]

if mv <= (n+1)//2:
    print("YES")
else:
    print("NO")
