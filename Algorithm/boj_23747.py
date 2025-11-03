# boj_23747.py
# 와드

from collections import deque
import sys

input = sys.stdin.readline


def lighting(si, sj, word):
    queue = deque([(si, sj)])
    matrix[si][sj] = "."
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + delta[k][0]
            nj = j + delta[k][1]
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == word:
                queue.append((ni, nj))
                matrix[ni][nj] = "."


N, M = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(N)]
si, sj = map(int, input().split())
si -= 1
sj -= 1
works = list(map(str, input().strip()))
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for move in works:
    if move == "U":
        si += delta[0][0]
        sj += delta[0][1]
    elif move == "D":
        si += delta[1][0]
        sj += delta[1][1]
    elif move == "L":
        si += delta[2][0]
        sj += delta[2][1]
    elif move == "R":
        si += delta[3][0]
        sj += delta[3][1]
    elif move == "W":
        if matrix[si][sj] == ".":
            continue
        lighting(si, sj, matrix[si][sj])

for k in range(4):
    ni = si + delta[k][0]
    nj = sj + delta[k][1]
    if 0 <= ni < N and 0 <= nj < M:
        matrix[ni][nj] = "."
matrix[si][sj] = "."

for i in range(N):
    now_line = []
    for j in range(M):
        if matrix[i][j] == ".":
            now_line.append(".")
        else:
            now_line.append("#")
    print("".join(map(str, now_line)))
