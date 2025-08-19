# swea_9489.py
# 고대 유적

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    visits = set()
    max_len = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                now_j_len = 0
                for jj in range(j, M):
                    if matrix[i][jj] == 1:
                        now_j_len += 1
                    else:
                        break
                now_i_len = 0
                for ii in range(i, N):
                    if matrix[ii][j] == 1:
                        now_i_len += 1
                    else:
                        break
                if now_i_len == 1:
                    now_i_len = 0
                if now_j_len == 1:
                    now_j_len = 0
                max_len = max(max_len, now_j_len, now_i_len)
    print(f"#{case} {max_len}")

