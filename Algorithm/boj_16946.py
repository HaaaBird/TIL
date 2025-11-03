# boj_16946.py
# 0 기준으로 그룹화 한다음 자기 그룹의 숫자를 넣어두고
# 벽 만나면 상하좌우 그룹 숫자 다 더하면 될듯?


from collections import deque
import sys

input = sys.stdin.readline

def bfs(si, sj, g_idx):
    queue = deque([(si, sj)])
    visited = {(si, sj)}
    cnt = 0
    while queue:
        i, j = queue.popleft()
        cnt += 1
        for k in range(4):
            ni = i + delta[k][0]
            nj = j + delta[k][1]
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 0 and (ni, nj) not in visited:
                queue.append((ni, nj))
                visited.add((ni, nj))
    for gi, gj in visited:
        g_map[gi][gj].append((g_idx, cnt))


N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
g_map = [[[] for _ in range(M)] for _ in range(N)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
g_idx = 0

result_matrix = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0 and len(g_map[i][j]) == 0:
            bfs(i, j, g_idx)
            g_idx += 1

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            n_set = set()
            n_cnt = 1
            for k in range(4):
                ni = i + delta[k][0]
                nj = j + delta[k][1]
                if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 0 and len(g_map[ni][nj]) != 0:
                    ng_idx = g_map[ni][nj][0][0]
                    n_size = g_map[ni][nj][0][1]
                    if ng_idx not in n_set:
                        n_set.add(ng_idx)
                        n_cnt += n_size
            result_matrix[i][j] = n_cnt % 10
    print("".join(map(str, result_matrix[i])))

