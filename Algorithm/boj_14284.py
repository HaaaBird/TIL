from heapq import heappop, heappush
import sys
input = sys.stdin.readline

# boj_14284.py
def find(start_node):
    INF = 10 ** 21
    pq = [(0, start_node)]
    dists = [INF] * N

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


N, M = map(int, input().split())
graph_list = [list(map(int, input().split())) for _ in range(M)]
s_node, d_node = map(int, input().split())
graph = [[] for _ in range(N)]
s_node_flag = False
d_node_flag = False
for a, b, w in graph_list:
    if a == s_node or b == s_node:
        s_node_flag = True
    elif a == d_node_flag or b == d_node_flag:
        d_node_flag = True
    a -= 1
    b -= 1
    graph[a].append((w, b))
    graph[b].append((w, a))
    if s_node_flag and d_node_flag:
        break

a = find(s_node - 1)

print(a[d_node - 1])
