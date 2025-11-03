# swea_1249.py
# 보급로
"""
델타 돌면서 이동 가능한 위치 만들고
다익스트라
"""
from heapq import heappop, heappush


def dijkstar(si, sj):
    MAX = 10 ** 9
    queue = [(0, si, sj)]
    dists = [[MAX] * N for _ in range(N)]
    dists[si][sj] = 0

    while len(queue) != 0:
        dist, ni, nj = heappop(queue)
        if dists[ni][nj] < dist:
            continue
        for k in range(4):
            nni = ni + delta[k][0]
            nnj = nj + delta[k][1]
            if 0 <= nni < N and 0 <= nnj < N:
                new_dist = dist + matrix[nni][nnj]
                if dists[nni][nnj] <= new_dist:
                    continue
                dists[nni][nnj] = new_dist
                heappush(queue, (new_dist, nni, nnj))
    return dists


T = int(input())
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(N)]
    graph = [[[] for _ in range(N)] for _ in range(N)]
    a = dijkstar(0,0)
    print(f"#{case} {a[N-1][N-1]}")
