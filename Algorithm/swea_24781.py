# swea_24781.py
# 경건한 파리채


T = int(input())

for case in range(1, 1 + T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    result = 0
    best_i = 0
    best_j = 0
    for i in range(N):
        for j in range(N):
            temp_kill = matrix[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    temp_kill += matrix[ni][nj]
            if result < temp_kill:
                result = temp_kill
                best_i = i
                best_j = j
    print(f"#{case} {result} {best_i} {best_j}")
