# boj_6497.py
# 전력난
"""
양방향이라 프림으로 풀어야 하는거 같은디
"""
import sys

input = sys.stdin.readline
from heapq import heappop, heappush


def prim(start_node):
    queue = [(0, start_node)]
    MST = [0] * V
    result = 0

    while len(queue) != 0:
        n_weight, n_node = heappop(queue)
        if MST[n_node] == 1:
            continue
        result += n_weight
        MST[n_node] = 1

        for i_w, i_n in graph[n_node]:
            if MST[i_n] == 1:
                continue
            heappush(queue, (i_w, i_n))
    return result


while True:
    V, E = map(int, input().split())
    if V == 0 and E == 0:
        break
    graph = [[] for _ in range(V)]
    max_val = 0
    for _ in range(E):
        a, b, w = map(int, input().split())
        max_val += w
        graph[a].append((w, b))
        graph[b].append((w, a))
    result = prim(0)
    print(max_val - result)
