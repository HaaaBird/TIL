# swea_12712.py
# 파리퇴치 3

T = int(input())
for case in range(1, 1 + T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    di_p = [0,1,0,-1] # 동 -> 남 -> 서 -> 북
    dj_p = [1,0,-1,0]

    di_x = [-1, 1, 1, -1] # 북동 -> 남동 -> 님서 -> 북서
    dj_x = [1, 1, -1, -1]

    kill_max = 0

    for i in range(N):
        for j in range(N):
            temp_sums = [matrix[i][j], matrix[i][j]]
            for k in range(1,M):
                for c in range(4):
                    ni_p = i+di_p[c]*k
                    nj_p = j+dj_p[c]*k
                    ni_x = i+di_x[c]*k
                    nj_x = j+dj_x[c]*k
                    if 0 <= ni_p < N and 0 <= nj_p < N:
                        temp_sums[0] += matrix[ni_p][nj_p]
                    if 0 <= ni_x < N and 0 <= nj_x < N:
                        temp_sums[1] += matrix[ni_x][nj_x]
            if kill_max < max(temp_sums):
                kill_max = max(temp_sums)
    print(f"#{case} {kill_max}")
