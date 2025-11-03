# boj_1939.py
# 중량제한

"""
이동을 하면서 가중치가 가장 높은 다리를 선택하게 해서 가중치 합이 가장 큰 다익스트라를 그리게 해야 하는데

"""
from heapq import heappop, heappush


def find(start_node):
    dists = [1] * N
    pq = [(1, start_node)]

    while len(pq) != 0:
        dist, node = heappop(pq)
        if dists[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            new_dist = max(next_dist, dist)
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    return dists


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    w *= -1
    graph[a].append((w, b))
    graph[b].append((w, a))
start_node, destination_node = map(int, input().split())
a = find(start_node-1)
print(a)