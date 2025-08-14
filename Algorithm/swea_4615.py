# swea_4615.py
# 재밌는 오셀로 게임
"""
크기 작아서 완탐 해도 된다.
확인할 것은 8개 방향

방금 둔 돌 기준: 상하좌우 - 대각 4개방향

에 대해서 8번 검사하면 된다.
그냥 일반 델타 문제로 순회하면서 벽에 부딛힐때까지 진행하고.

지나가다가 시작한 돌이랑 다른색상 만나면 stack 에 쌓아두고
가다가 다시 나랑 똑같은 색상 만나면 stack 에 있던거 다 뒤집으면 된다.
"""
delta_map = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1], [1, 0], [1, 1]
]

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    game_log = [list(map(int, input().split())) for _ in range(M)]

    matrix = [[0] * N for _ in range(N)]
    matrix[len(matrix) // 2 - 1][len(matrix) // 2 - 1] = 2
    matrix[len(matrix) // 2 - 1][len(matrix) // 2] = 1
    matrix[len(matrix) // 2][len(matrix) // 2 - 1] = 1
    matrix[len(matrix) // 2][len(matrix) // 2] = 2

    for play in game_log:
        ni = play[1] - 1
        nj = play[0] - 1
        color = play[2]
        matrix[ni][nj] = color
        for direct in range(8):
            stack = []
            ri = ni + delta_map[direct][0]
            rj = nj + delta_map[direct][1]
            while 0 <= ri < N and 0 <= rj < N:
                if matrix[ri][rj] == 0:
                    break
                elif matrix[ri][rj] == color:
                    for _ in range(len(stack)):
                        wi, wj = stack.pop()
                        matrix[wi][wj] = color
                    break
                else:
                    stack.append((ri, rj))
                    ri += delta_map[direct][0]
                    rj += delta_map[direct][1]

    black_cnt = 0
    white_cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                black_cnt += 1
            elif matrix[i][j] == 2:
                white_cnt += 1
    print(f"#{case} {black_cnt} {white_cnt}")