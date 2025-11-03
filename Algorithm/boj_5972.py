# boj_5972.py
# 택배 배송
from heapq import heappop, heappush


def dijkstra(start_node):
    INF = 10**21
    pq = [(0, start_node)]
    dists = [INF] * N
    dists[start_node] = 0

    while len(pq) != 0:
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


N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((w, b))
    graph[b].append((w, a))

result = dijkstra(0)
print(result[N-1])
