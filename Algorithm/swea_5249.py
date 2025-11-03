# swea_5249.py
# 최소 신장 트리
from heapq import heappush, heappop
def prim(start_node):
    pq = [(0, start_node)]
    MST = [0] * V
    min_weight = 0

    while len(pq) != 0:
        n_w, n_n = heappop(pq)

        if MST[n_n]:
            continue
        MST[n_n] = 1
        min_weight += n_w

        for next_node in range(V):
            if graph[n_n][next_node] == 0:
                continue
            if MST[next_node]:
                continue
            heappush(pq, (graph[n_n][next_node], next_node))

    return min_weight

T = int(input())
for case in range(1, T + 1):
    V, E = map(int, input().split())
    V += 1
    graph = [[0] * V for _ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w
    result = prim(0)
    print(f"#{case} {result}")