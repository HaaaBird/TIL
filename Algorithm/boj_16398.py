# boj_16398.py
# 행성

"""
최소 스패닝 트리를 만드는 문제
"""
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def prim(start_node):
    queue = [(0, start_node)]
    MST = [0] * N
    min_result = 0

    while len(queue):
        n_w, n_node = heappop(queue)
        if MST[n_node] == 1: # 이미 방문 했다면 중단
            continue
        MST[n_node] = 1 # 갱신
        min_result += n_w
        for i in range(N):
            if graph[n_node][i] == 0:
                continue
            if MST[i] == 1:
                continue
            heappush(queue, (graph[n_node][i], i))
    return min_result


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
a = prim(0)
print(a)
