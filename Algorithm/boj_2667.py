# boj_2667.py
# 단지 번호 붙이기


N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)]
visit_map = [[-1] * N for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
result = []

# matrix 순회하면서 bfs로 이어진 경로 탐색. 이후 하나씩 카운팅?

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visit_map[i][j] != 1:
            queue = [(i, j)]
            visit = 1
            head = 0
            visit_map[i][j] = 1
            # 여기서 bfs 시작.
            while len(queue) > head:
                now = queue[head]
                head += 1
                ii = now[0]
                jj = now[1]
                for k in range(4):
                    ni = ii + di[k]
                    nj = jj + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] != 0:
                        if matrix[ni][nj] == 1 and visit_map[ni][nj] != 1:
                            queue.append((ni, nj))
                            visit += 1
                            visit_map[ni][nj] = 1
            result.append(visit)
result.sort()
print(len(result))
for val in result:
    print(val)
