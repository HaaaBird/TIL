# swea_4615.py
# 재밌는 오셀로 게임
"""
크기 작아서 완탐 해도 된다.
확인할 것은 8개 방향

방금 둔 돌 기준: 상하좌우 - 대각 4개방향
에 대해서 8번 검사하면 된다.

종료 조건은.

나랑 같은 색깔의 돌을 만나면 종료
탐색 영역이 초과되면 종료
그 이전까지 나랑 다른 색깔의 돌을 담아둔 리스트 가지고 있다가
해당 리스트 안에 있는 돌들은 모두 뒤집기

b:1 w:2
"""
delta_map = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
]


def check_8(i, j, matrix, color):
    for d in range(8):  # 방향 결정
        ni, nj = i, j
        turn = []
        for p in range(1, N):
            ni += delta_map[d][0]
            nj += delta_map[d][1]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                break
            elif matrix[ni][nj] != 0 and matrix[ni][nj] != color:
                turn.append((ni, nj))
                continue
            elif matrix[ni][nj] == color:
                turn.append((ni, nj))
                break
            else:
                break
        if len(turn) != 0 and matrix[turn[-1][0]][turn[-1][1]] == color:
            for ti, tj in turn:
                matrix[ti][tj] = color


T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]
    play_log = [list(map(int, input().split())) for _ in range(M)]
    # 처음에 돌 4개 놓기
    matrix[N // 2 - 1][N // 2 - 1] = 2
    matrix[N // 2 - 1][N // 2] = 1
    matrix[N // 2][N // 2 - 1] = 1
    matrix[N // 2][N // 2] = 2
    # j i color
    # 1 2 1
    for play in play_log:
        i = play[1] - 1
        j = play[0] - 1
        color = play[2]
        # 돌 착수
        matrix[i][j] = color
        check_8(i,j,matrix,color)

    black_cnt, white_cnt = 0, 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                black_cnt += 1
            elif matrix[i][j] == 2:
                white_cnt += 1

    print(f"#{case} {black_cnt} {white_cnt}")

