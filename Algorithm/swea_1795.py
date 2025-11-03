# swea_1795.py
# 인수의 생일파티
"""
각 노드 단위로 다익스트라 돌리는데, 타겟 노드는 끝까지 다 돌리고
나머지 노드들은 타겟 노드에 도달하기까지 걸린 시간만 return

그 다음에 그거 더해서 최대값 리턴
"""
from heapq import heappop, heappush
def d_cut(start, target):
    queue = [(0, start)]
    dists = [INF] * N
    dists[start] = 0

    while len(queue) != 0:
        dist, node = heappop(queue)
        if node == target:
            return dist
        if dists[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            new_dist = next_dist + dist
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            heappush(queue, (new_dist, next_node))

def full_d(start):
    queue = [(0, start)]
    dists = [INF] * N
    dists[start] = 0

    while len(queue) != 0:
        dist, node = heappop(queue)
        if dists[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            new_dist = next_dist + dist
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            heappush(queue, (new_dist, next_node))
    return dists

INF = 10**21
T = int(input())
for case in range(1, T + 1):
    N, M, X = map(int, input().split())
    X -= 1
    graph = [[] for _ in range(M)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        s -= 1
        e -= 1
        graph[s].append((w, e))
    full_list = full_d(X)
    result = 0
    for i in range(N):
        if i == X:
            continue
        else:
            a = d_cut(i, X)
            result = max(result, a + full_list[i])
    print(f"#{case} {result}")