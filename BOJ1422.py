# BOJ 1422
import sys
from functools import cmp_to_key

# BOJ 16496 과 유사한 문제로 같은 정렬 함수를 사용했는데
# 21%에서 계속 오답이 되어 다른 방법을 사용함
def compare(a,b):
    return int(b+a) - int(a+b)

K, N=map(int, sys.stdin.readline().split())
num=[]
num_max=0
for _ in range(K):
    tmp=sys.stdin.readline().rstrip()
    num.append(tmp)
    if num_max < int(tmp):
        num_max=int(tmp)
num_max=str(num_max)
for _ in range(N-K):
    num.append(num_max)
num.sort(key=cmp_to_key(compare))
print(*num, sep='')