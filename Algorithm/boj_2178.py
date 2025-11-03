# boj_2178.py
# 미로

N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visit = {(0, 0)}
queue = [(0,0,0)]
head = 0
result = 0
while head < len(queue):
    i, j, dist = queue[head]
    head += 1
    if i == N-1 and j == M-1:
        result = dist + 1
        break
    for k in range(4):
        ni = i + delta[k][0]
        nj = j + delta[k][1]
        if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 1 and (ni, nj) not in visit:
            queue.append((ni, nj, dist + 1))
            visit.add((ni, nj))

print(result)