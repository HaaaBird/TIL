# boj_1647.py
# 도시 분할 계획
"""
스패닝 트리 구성하면서 가중치 가장 높은거 갱신한다음
마지막에 그거 빼 주면 되는거 아닌가?
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def prim(s_node):
    queue = [(0, s_node)]
    MST = [0] * N
    result_weight = 0
    max_weight = 0
    while len(queue) != 0:
        n_weight, n_node = heappop(queue)
        if MST[n_node] != 0:
            continue
        MST[n_node] = 1
        result_weight += n_weight
        max_weight = max(max_weight, n_weight)
        for i_weight, i_node in graph[n_node]:
            if MST[i_node] != 0: # 방문 이미 했다면
                continue
            heappush(queue, (i_weight, i_node))
    return result_weight, max_weight

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((w, v))
    graph[v].append((w, u))

a, b = prim(0)
print(a - b)