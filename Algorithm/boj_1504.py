# boj_1504.py
# 특정한 최단경로

"""
반드시 찍은 두개 경로를 통과해야 한다.
"""
from heapq import heappop, heappush
def dijkstra(start):
    pq = [(0, start)]

    dists = [INF] * N
    dists[start] = 0

    while pq:
        dist, node = heappop(pq)
        if dists[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            new_dist = next_dist + dist
            if dists[next_node] <= new_dist:
                continue
            heappush(pq, (new_dist, next_node))
            dists[next_node] = new_dist
    return dists


N, E = map(int, input().split())
graph = [[] for _ in range(N)]
INF = 10 ** 21
for _ in range(E):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((w, b))
    graph[b].append((w, a))

ta, tb = map(int, input().split())
ta -= 1; tb -= 1
d_start = dijkstra(0)
d_ta = dijkstra(ta)
d_tb = dijkstra(tb)

case_a = d_start[ta] + d_ta[tb] + d_tb[N-1]
case_b = d_start[tb] + d_tb[ta] + d_ta[N-1]

result = min(case_a, case_b)
if result >= INF:
    print(-1)
else:
    print(result)

