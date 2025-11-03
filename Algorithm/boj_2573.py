# boj_2573.py
# 빙산
from collections import deque
from pprint import pprint


def bfs(si, sj):
    queue = deque([(si, sj)])
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + delta[k][0]
            nj = j + delta[k][1]
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] != 0 and visit_map[ni][nj] == 0:
                queue.append((ni, nj))
                visit_map[ni][nj] = True


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visit_map = [[0] * M for _ in range(N)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

work_cnt = 0
while True:
    # 빙산 숫자 세기
    work_cnt += 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0 and visit_map[i][j] == 0:
                bfs(i, j)
                cnt += 1
    if cnt <= 2:
        break
    del_list = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                zero_cnt = 0
                for k in range(4):
                    ni = i + delta[k][0]
                    nj = j + delta[k][1]
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 0:
                        zero_cnt += 1
                del_list.append((i, j, zero_cnt))

    for di, dj, c in del_list:
        matrix[di][dj] = max(matrix[di][dj] - c, 0)
    print(work_cnt)
    pprint(matrix)

print(work_cnt)
