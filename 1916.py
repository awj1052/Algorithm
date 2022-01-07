import sys; r=sys.stdin.readline
import heapq
def dijkstra(start):
    heap=[]
    heapq.heappush(heap, (0,start))
    while heap:
        c, s = heapq.heappop(heap)
        if distance[s] < c: continue
        for i_s, i_c in cost[s]:
            if c + i_c >= distance[i_s]: continue
            distance[i_s] = c + i_c
            heapq.heappush(heap, (distance[i_s], i_s))

INF=int(1e9)
N=int(r())
cost=[[] for _ in range(N+1)]
for _ in range(int(r())):
    a,b,c=map(int,r().split())
    cost[a].append([b,c])

start,end=map(int,r().split())
distance=[INF]*(N+1)
distance[start]=0
dijkstra(start)

print(distance[end])
