# boj_1520.py
# 내리막길
import sys
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
result = 0
visited[0][0] = True

stack = [(0,0)]

while len(stack) != 0:
    i, j = stack.pop()
    if i == M-1 and j == N-1:
        result += 1
        continue
    for k in range(4):
        ni = i + delta[k][0]
        nj = j + delta[k][1]
        if 0 <= ni < M and 0 <= nj < N and matrix[ni][nj] < matrix[i][j] and matrix[ni][nj] is not True:
            visited[ni][nj] = True
            stack.append((ni, nj))
        else:
            visited[ni][nj] = True


print(result)