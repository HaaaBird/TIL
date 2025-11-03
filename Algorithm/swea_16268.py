# swea_16268.py
# 풍선팡

delta_map = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N):
        for j in range(M):
            now_sum = matrix[i][j]
            for k in range(4):
                ni = i + delta_map[k][0]
                nj = j + delta_map[k][1]
                if 0 <= ni < N and 0 <= nj < M:
                    now_sum += matrix[ni][nj]
            max_sum = max(max_sum, now_sum)
    print(f"#{case} {max_sum}")