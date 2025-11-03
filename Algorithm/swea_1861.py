# swea_1861.py
# 정사각형 방


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_room(i, j, cnt, sn):
    global result_cnt, result_start
    for k in range(4):
        ni = i + delta[k][0]
        nj = j + delta[k][1]
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] - 1 == matrix[i][j] and visited[ni][nj] is not True:
            visited[ni][nj] = True
            find_room(ni, nj, cnt + 1, sn)

    if result_cnt <= cnt:
        if result_cnt < cnt:
            result_start = sn
            result_cnt = cnt
        elif result_cnt == cnt:
            if result_start > sn:
                result_start = sn
    return


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result_cnt = 0
    result_start = 100000

    for i in range(N):
        for j in range(N):
            if visited[i][j] is True:
                continue
            find_room(i, j, 1, matrix[i][j])

    print(f"#{case} {result_start} {result_cnt}")
