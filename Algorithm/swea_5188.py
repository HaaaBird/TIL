# swea_5188.py
# 최소합

delta = [(1, 0), (0, 1)]


def backT(si, sj, cost):
    global result_cost
    cost += matrix[si][sj]
    if si == N - 1 and sj == N - 1:
        result_cost = min(result_cost, cost)
        return

    if cost > result_cost:
        return
    for k in range(2):
        ni = si + delta[k][0]
        nj = sj + delta[k][1]
        if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] is False:
            visit[ni][nj] = True
            backT(ni, nj, cost)
            visit[ni][nj] = False

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    result_cost = 10 ** 9
    backT(0, 0, 0)
    print(f"#{case} {result_cost}")
