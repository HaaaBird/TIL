# swea_1949.py
# 등산로 조성

"""
백트래킹 두번 써야함
1. 델타를 선택하는 백트래킹
2. 땅을 팔지 말지 고르는 백트래킹

그러면 땅 선택 조건이 현 상태에 땅 팔 수 있는 쿠폰이 있는가?
    있다면 땅 파서 낮출 수 있는 땅도 선택해서 백트래킹
    없다면 나보다 낮은 땅에 대해서만 백트래킹
"""
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def backT(i, j, can_dig, dig_now, n_length):
    global max_length
    max_length = max(max_length, n_length)

    if dig_now != 0:  # 땅 파라는 오더가 있다면 땅 파고 다시 재귀
        matrix[i][j] -= dig_now
        backT(i, j, 0, 0, n_length)
        matrix[i][j] += dig_now
        return
    for k in range(4):
        ni = i + delta[k][0]
        nj = j + delta[k][1]
        # 땅 파기 가능 여부를 떠나 가능하다면 현 상태 그대로 다시 백트래킹 진입
        if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] is False and matrix[ni][nj] < matrix[i][j]:
            visit[ni][nj] = True
            backT(ni, nj, can_dig, 0, n_length + 1)  # 다음 턴에 땅 안파기. 굳이 땅 팔 이유가 없음
            visit[ni][nj] = False
        # 땅 파기 하면 갈 수 있고 땅 팔 수 있다면
        elif 0 <= ni < N and 0 <= nj < N and visit[ni][nj] is False and (matrix[ni][nj] - K) < matrix[i][j] and can_dig == 1:
            visit[ni][nj] = True
            backT(ni, nj, 0, matrix[ni][nj] - matrix[i][j] + 1, n_length + 1)  # 땅 파기 쿠폰 날리고 땅 파라는 오더와 함께 진입. 최소 파야 하는 깊이
            visit[ni][nj] = False
    return


T = int(input())
for case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_height = 0
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        max_height = max(max_height, max(matrix[i]))

    max_length = 1
    for oi in range(N):
        for oj in range(N):
            if matrix[oi][oj] == max_height:
                visit[oi][oj] = True
                backT(oi, oj, 1, 0, 1)
                visit[oi][oj] = False
    print(f"#{case} {max_length}")
