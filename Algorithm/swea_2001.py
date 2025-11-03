# swea_2001.py
# 파리 퇴치

T = int(input())
for case in range(1, T+1):
    matrix = []
    N, M = map(int, input().split())
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    # 2중 for 문을 통한 2차원 배열 접근
    max_kill = 0
    for i in range(N):
        for j in range(N):
            n_kill = 0
            for ni in range(i, i+M):
                for nj in range(j, j+M):
                    if ni < N and nj < N: # 확장값만 보는 것임으로 N을 초과(인덱스 초과)하는 것만 방지
                       n_kill += matrix[ni][nj]
            if n_kill > max_kill:
                max_kill = n_kill
    print(f"#{case} {max_kill}")