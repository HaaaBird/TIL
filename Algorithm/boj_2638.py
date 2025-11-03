# boj_2638.py
# 치즈

"""
좌측 모서리에서 bfs 탐색 해서
좌측 모서리와 연결된 모든 칸은 -1로 처리.

그 다음 다시 순회하며 -1과 접촉한 칸이 2개 이상인 치즈 다 썰면서 -1로 처리

for 문 순회하다 0 만나면 거기서부터 다시
"""


def search_air(si, sj):
    queue = deque([(si, sj)])
    visited = [[False] * M for _ in range(N)]
    visited[si][sj] = True

    while len(queue) != 0:
        ni, nj = queue.popleft()
        matrix[ni][nj] = 9
        for k in range(4):
            nni = ni + delta[k][0]
            nnj = nj + delta[k][1]
            if 0 <= nni < N and 0 <= nnj < M and (matrix[nni][nnj] == 0 or matrix[nni][nnj] == 9) and visited[nni][
                nnj] is False:
                queue.append((nni, nnj))
                visited[nni][nnj] = True


from collections import deque
from pprint import pprint

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
total = 1

search_air(0, 0)
while True:
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                cnt = 0
                for k in range(4):
                    ni = i + delta[k][0]
                    nj = j + delta[k][1]
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 9:
                        cnt += 1
                    if cnt == 2:
                        matrix[i][j] = 0
                        break
    flag = True
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                flag = False
                break
        if flag is False:
            break
    if flag is False:
        search_air(0, 0)
        total += 1
    else:
        break

print(total)
