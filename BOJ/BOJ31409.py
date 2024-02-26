n = int(input())
a = [0] + list(map(int,input().split()))

ans=0
if a[1] == 1:
    a[1] = 2
    ans = 1
for i in range(2, n+1):
    if a[i] == i:
        a[i] = 1
        ans += 1
print(ans)
print(*a[1:])
