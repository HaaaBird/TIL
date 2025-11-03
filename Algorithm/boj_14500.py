# boj_14500.py
# 테크로미노
"""

하나 빼고 다 그냥 델타로 직진 돌려서 이동거리 계산해도 됨. 어차피 직진만으로 만들 수 있음.
법규모양만 이 빠진 델타로 새롭게 잡아서 해야할듯?
그냥 뎁스가 4인것 까지 조사하게 하면 됨. 모든 좌표에 대해서

시간 제한 2초인데 돌아가려나?
"""

import sys
input = sys.stdin.readline


def dfs(i, j, depth, total_score):
    global max_value
    if depth == 4:
        max_value = max(max_value, total_score)
        return
    for d in range(4):
        ni = i + delta[d][0]
        nj = j + delta[d][1]
        if 0 <= ni < N and 0 <= nj < M and not visits[ni][nj]:
            visits[ni][nj] = True
            dfs(ni, nj, depth + 1, total_score + matrix[ni][nj])
            visits[ni][nj] = False


def delta_search(si, sj):
    total_max = 0
    for i in range(4):
        n_score = [matrix[si][sj]]
        for j in range(3):
            nd = (i + j) % 4
            ni = si + delta[nd][0]
            nj = sj + delta[nd][1]
            if 0 <= ni < N and 0 <= nj < M:
                n_score.append(matrix[ni][nj])
            else:
                break
        if len(n_score) == 4:
            total_max = max(total_max, sum(n_score))
    return total_max


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visits = [[False] * M for _ in range(N)]
max_value = 0

for i in range(N):
    for j in range(M):
        visits[i][j] = True
        dfs(i, j, 1, matrix[i][j])
        visits[i][j] = False
        max_value = max(max_value, delta_search(i, j))

print(max_value)
