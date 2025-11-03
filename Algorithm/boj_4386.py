# boj_4386.py
# 별자리 만들기
"""
대각선 거리 삼각측량해서 가중치로 쓰라는 소리같은데
별 갯수가 100개, 100 x 100 해서 1만번 순회 돌아야 할듯?
"""
import math
from heapq import heappop, heappush
import sys

input = sys.stdin.readline

def get_dist(start_s, end_s):
    dx = abs(start_s[0] - end_s[0])
    dy = abs(start_s[1] - end_s[1])
    return math.hypot(dx, dy)

def prim(start_node):
    queue = [(0, start_node)] # 가중치, 시작노드
    MST = [0] * N
    result = 0
    while len(queue) != 0:
        n_weight, n_node = heappop(queue)
        if MST[n_node] == 1:
            continue
        result += n_weight
        MST[n_node] = 1

        for node_idx in range(N):
            if MST[node_idx] == 1:
                continue
            heappush(queue, (graph[n_node][node_idx], node_idx))
    return result

N = int(input())
graph = [[0] * N for _ in range(N)]
stars = [list(map(float, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        dist = get_dist(stars[i], stars[j])
        graph[i][j] = dist
        graph[j][i] = dist
f_result = prim(0)
print(f"{f_result:.2f}")