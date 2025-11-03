# swea_5251.py
# 최소 이동 거리
from heapq import heappush, heappop


def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [10 ** 9] * N
    dists[start_node] = 0

    while len(pq) != 0:
        dist, node = heappop(pq)
        if dists[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            n_dist = dist + next_dist
            if dists[next_node] <= n_dist:
                continue
            dists[next_node] = n_dist
            heappush(pq, (n_dist, next_node))
    return dists


T = int(input())
for case in range(1, T + 1):
    N, E = map(int, input().split())
    N += 1
    graph = [[] for _ in range(N)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    result = dijkstra(0)
    print(f"#{case} {result[N - 1]}")
