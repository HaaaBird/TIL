# swea_20739.py
# 고대 유적

"""
그냥 가장 긴 1을 찾아서 출력
값이 1이면 0 출력
"""


T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0

    # 행 단위 검색
    for i in range(N):
        now_len = 0
        for j in range(M):
            if matrix[i][j] != 0:
                now_len += 1
            else:
                max_len = max(now_len, max_len)
                now_len = 0
            if j == M-1:
                max_len = max(now_len, max_len)

    # 열 단위 검색
    for j in range(M):
        now_len = 0
        for i in range(N):
            if matrix[i][j] != 0:
                now_len += 1
            else:
                max_len = max(now_len, max_len)
                now_len = 0
            if i == N-1:
                max_len = max(now_len, max_len)
    if max_len == 1:
        max_len = 0

    print(f"#{case} {max_len}")
