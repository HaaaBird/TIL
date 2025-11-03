# swea_20230.py
# 풍선팡 보너스게임2


"""
풍선을 터트리면 행과 열이 다 터진다. -> 델타 써서 다 죽여라
"""
di = [0, 1 ,0 ,-1]
dj = [1, 0, -1, 0]

T = int(input())
for case in range(1, 1 + T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    for i in range(N):
        for j in range(N):
            now_score = matrix[i][j]
            for c in range(1, N):
                for d_idx in range(4):
                    ni = i + di[d_idx] * c
                    nj = j + dj[d_idx] * c
                    if 0 <= ni < N and 0 <= nj < N:
                        now_score += matrix[ni][nj]
            max_score = max(max_score, now_score)
    print(f"#{case} {max_score}")