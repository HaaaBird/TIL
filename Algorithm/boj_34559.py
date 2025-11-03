# boj_34559.py
# 건물 (누적합 버전 - cnt 포함)

from collections import deque
import sys
input = sys.stdin.readline
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(si, sj):
    queue = deque([(si, sj)])
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + delta[k][0]
            nj = j + delta[k][1]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1


def point_check(arr):
    if arr[0] - arr[2] >= 0 and arr[1] - arr[3] <= 0:
        return [arr[2], arr[0], arr[1], arr[3]]
    elif arr[0] - arr[2] >= 0 and arr[1] - arr[3] >= 0:
        return [arr[2], arr[0], arr[3], arr[1]]
    elif arr[0] - arr[2] <= 0 and arr[1] - arr[3] >= 0:
        return [arr[0], arr[2], arr[3], arr[1]]
    elif arr[0] - arr[2] <= 0 and arr[1] - arr[3] <= 0:
        return [arr[0], arr[2], arr[1], arr[3]]

N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
visited = [arr[:] for arr in matrix]
Q = int(input())
orders = [list(map(int, input().split())) for _ in range(Q)]

for i in [0, N - 1]:
    for j in range(M):
        if visited[i][j] == 0:
            bfs(i, j)
for i in range(N):
    for j in [0, M - 1]:
        if visited[i][j] == 0:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            matrix[i][j] = 1

prefix = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = (
            matrix[i - 1][j - 1]
            + prefix[i - 1][j]
            + prefix[i][j - 1]
            - prefix[i - 1][j - 1]
        )


def rect_sum(r1, c1, r2, c2):
    return prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]

for i in range(Q):
    i_arr = point_check(orders[i])
    cnt = rect_sum(i_arr[0], i_arr[2], i_arr[1], i_arr[3])
    if cnt == 0:
        print("Yes")
    else:
        print(f"No {cnt}")
