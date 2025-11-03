from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs1(si, sj, s_depth):
    visit = {(si, sj)}
    queue = deque([(si, sj, s_depth)])
    while len(queue) != 0:
        i, j, depth = queue.popleft()
        if matrix[i][j] == "L":
            if dist[i][j] == 0:
                dist[i][j] = depth
            else:
                dist[i][j] = min(dist[i][j], depth)
        for k in range(4):
            ni = i + delta[k][0]
            nj = j + delta[k][1]
            if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visit and matrix[ni][nj] != "W":
                queue.append((ni, nj, depth + 1))
                visit.add((ni, nj))


T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(N)]
    dist = [[0] * M for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "W":
                bfs1(i, j, 0)

    for i in range(N):
        result += sum(dist[i])
    print(f"#{case} {result}")