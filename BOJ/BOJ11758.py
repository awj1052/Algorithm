# 점 p1과 p2를 통과하는 직선을 l이라 할 때,
# p3가 l보다 위에 있으면 (v>0) 시계방향

# CCW (Counter Clock Wise) 알고리즘이 있음
# 두 벡터의 외적 값의 부호에 따라 어느 방향인지도 알 수 있음

x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

v = (y2-y1)*(x3-x1) + (x2-x1)*(y1-y3)
if v>0:
  print(-1)
elif v<0:
  print(1)
else:
  print(0)
