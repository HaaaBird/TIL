# swea_5105.py
# 미로의 거리


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(N)]
    s_ij = None
    e_ij = None
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:  # 출발지점
                s_ij = (i, j)
            elif matrix[i][j] == 3: # 도착지점
                e_ij = (i, j)
    result = 0
    queue = [(s_ij[0], s_ij[1], 0)]
    visits = set()
    while len(queue) != 0:
        now = queue.pop(0)
        i = now[0]
        j = now[1]
        dist = now[2]
        visits.add((i, j))
        if matrix[i][j] == 3:
            result = dist - 1
            break
        for k in range(4):
            ni = i + delta[k][0]
            nj = j + delta[k][1]
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visits:
                if matrix[ni][nj] != 1:
                    queue.append((ni, nj, dist+1))
    print(result)