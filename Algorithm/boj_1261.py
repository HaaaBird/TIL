# boj_1261.py
# 알고스팟

"""
벽을 부순다 -> 가중치가 올라간다로 생각하면 그냥 다익스트라 때리면 풀리는 문제 아니냐
"""
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra():
    pq = [(0, 0, 0)]
    INF = 10 ** 9
    dists = [[INF] * M for _ in range(N)]
    dists[0][0] = 0
    while len(pq) != 0:
        w, i, j = heappop(pq)
        if dists[i][j] < w:
            continue
        for next_w, next_i, next_j in graph[i][j]:
            new_w = w + next_w
            if dists[next_i][next_j] <= new_w:
                continue
            dists[next_i][next_j] = new_w
            heappush(pq, (new_w, next_i, next_j))
    return dists


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
M, N = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]

graph = [[[] for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + delta[k][0]
            nj = j + delta[k][1]
            if 0 <= ni < N and 0 <= nj < M:
                w = 0
                if matrix[ni][nj] == 1:
                    w += 1
                graph[i][j].append((w, ni, nj))
result = dijkstra()
print(result[N-1][M-1])
