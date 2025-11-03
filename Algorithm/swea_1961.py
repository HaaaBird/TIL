# swea_1961.py
# 숫자 회전


T = int(input())

for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    T1 = [[0] * N for _ in range(N)]
    T2 = [[0] * N for _ in range(N)]
    T3 = [[0] * N for _ in range(N)]

    offset = 0
    for i in range(N):
        for j in range(N):
            # j = ii
            # -1 * i + 2 = jj
            ni = j
            nj = -1 * i + (N-1)
            T1[ni][nj] = matrix[i][j]

    for i in range(N):
        for j in range(N):
            # j = ii
            # -1 * i + 2 = jj
            ni = j
            nj = -1 * i + (N-1)
            T2[ni][nj] = T1[i][j]

    for i in range(N):
        for j in range(N):
            # j = ii
            # -1 * i + 2 = jj
            ni = j
            nj = -1 * i + (N-1)
            T3[ni][nj] = T2[i][j]
    print(f"#{case}")
    # 각 i행마다: T1[i] 붙여쓰기, 공백, T2[i] 붙여쓰기, 공백, T3[i] 붙여쓰기
    for i in range(N):
        s1 = ''.join(str(x) for x in T1[i])
        s2 = ''.join(str(x) for x in T2[i])
        s3 = ''.join(str(x) for x in T3[i])
        print(s1, s2, s3)
