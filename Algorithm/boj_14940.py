# boj_14940.py
# 쉬운 최단거리


"""

문제
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

입력
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)
다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

출력
각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

각 셀마다 목적지 까지 도달하는 bfs 문제 구하기
"""


def find_start(matrix, N, M):
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                return i, j


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dist_matrix = [[-1] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            dist_matrix[i][j] = 0

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

s_ij = find_start(matrix, N, M)

# BFS
queue = [(s_ij[0], s_ij[1], 0)]
dist_matrix[s_ij[0]][s_ij[1]] = 0  # 시작점 거리 0으로 방문 확정
head = 0

while head < len(queue):
    i, j, dist = queue[head]
    head += 1
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            if matrix[ni][nj] != 0 and dist_matrix[ni][nj] == -1:
                dist_matrix[ni][nj] = dist + 1   # 방문(거리) 확정
                queue.append((ni, nj, dist + 1))

# 출력 형식 맞추기
for row in dist_matrix:
    print(' '.join(map(str, row)))
