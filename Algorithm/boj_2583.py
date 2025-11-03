# boj_2583.py
# 영역 칠하기
import pprint
from collections import deque
import sys
input = sys.stdin.readline
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(i, j):
    queue = deque([(i, j)])
    matrix[i][j] = 99
    result_size = 1
    while len(queue) != 0:
        si, sj = queue.popleft()
        for k in range(4):
            ni = si + delta[k][0]
            nj = sj + delta[k][1]
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 0:
                queue.append((ni, nj))
                matrix[ni][nj] = 99
                result_size += 1
    return result_size

N, M, K = map(int, input().split())
rec_list = [list(map(int, input().split())) for _ in range(K)]

matrix = [[0] * M for _ in range(N)]

for sj, si, ej, ei in rec_list:
    for new_i in range(si, ei):
        for new_j in range(sj, ej):
            matrix[new_i][new_j] += 1

result = 0
size = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            result += 1
            size.append(bfs(i, j))
size.sort()
print(result)
print(*size)