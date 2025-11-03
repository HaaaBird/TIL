# swea_5250.py
# 최소 비용
"""
델타 써서 각 셀에 방문하는 비용을 그래프 형태로 표현하고
다익스트라 돌려서 시작 노드(0, 0), 끝 노드(N-1, N-1)에 도달하는 비용 찾으면 될 듯?
"""
import pprint
import heapq


def dijkstra(s_i, s_j):
    INF = 10 ** 9
    pq = [(0, s_i, s_j)]
    dists = [[INF] * N for _ in range(N)]
    dists[s_i][s_j] = 0

    while len(pq) != 0:
        dist, i, j = heapq.heappop(pq)
        if dists[i][j] < dist:
            continue
        for next_dist, ni, nj in graph[i][j]:
            new_dist = dist + next_dist
            if dists[ni][nj] <= new_dist:
                continue
            dists[ni][nj] = new_dist
            heapq.heappush(pq, (new_dist, ni, nj))
    return dists


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    graph = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + delta[k][0]
                nj = j + delta[k][1]
                if 0 <= ni < N and 0 <= nj < N:
                    if matrix[ni][nj] > matrix[i][j]:  # 더 높으면
                        graph[i][j].append((1 + matrix[ni][nj] - matrix[i][j], ni, nj))
                    else:
                        graph[i][j].append((1, ni, nj))
    result = dijkstra(0, 0)
    print(f"#{case} {result[N-1][N-1]}")
