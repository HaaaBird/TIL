# boj_21736.py
# 헌내기는 친구가 필요해

from collections import deque
import sys

input = sys.stdin.readline
"""그냥 bfs로 순회하다 더 할꺼 없으면 pass"""
N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
user_ij = None

user_find = False
for i in range(N):
    if user_find:
        break
    for j in range(M):
        if matrix[i][j] == "I":
           user_ij = (i,j)
           visit[i][j] = True
           user_find = True
           break

queue = deque([user_ij])
meet_cnt = 0
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while len(queue):
    i, j = queue.popleft()
    if matrix[i][j] == "P":
        meet_cnt += 1
    for k in range(4):
        ni = i + delta[k][0]
        nj = j + delta[k][1]
        if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] != "X" and visit[ni][nj] is not True:
            queue.append((ni, nj))
            visit[ni][nj] = True


if meet_cnt == 0:
    print("TT")
else:
    print(meet_cnt)
