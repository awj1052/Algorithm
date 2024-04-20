# 핵심 아이디어
# n의 범위가 5000보다 작거나 같은데 시간제한은 1초이므로 O(N^2) 까지 가능하다고 생각
# 각 숫자의 범위가 생각보다 크지 않아 배열로 관리할 수 있음

n = int(input())
A = list(map(int, input().split()))
index = [[-1, -1] for _ in range(400_001)]
bias = 200_000

for i in range(n):
    for j in range(i, n):
        if index[A[i] + A[j] + bias][0] == -1:
            index[A[i] + A[j] + bias][0] = i
            index[A[i] + A[j] + bias][1] = j
        else:
            index[A[i] + A[j] + bias][0] = min(index[A[i] + A[j] + bias][0], i)
            index[A[i] + A[j] + bias][1] = min(index[A[i] + A[j] + bias][1], j)

ans = 0
for i in range(n):
    for j in range(i):
        if index[A[i] - A[j] + bias][0] == -1: continue
        if index[A[i] - A[j] + bias][0] >= i: continue
        if index[A[i] - A[j] + bias][1] >= i: continue
        ans+=1
        break
print(ans)
