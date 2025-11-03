# boj_14503.py
# 로봇 청소기

"""
방은 N x M 크기의 직사각형
각각의 칸은 벽 또는 빈 칸이다
방향은 동, 서, 남, 북


로봇 청소기는 다음과 같이 작동한다.

현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.

현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.

현재 칸의 주변
$4$칸 중 청소되지 않은 빈 칸이 있는 경우,
반시계 방향으로
$90^\circ$ 회전한다.
바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
1번으로 돌아간다.

1번조건은 델타 맵 k갱신하지 말고 그냥 현재 k기준으로 뒤집어서 한칸 뒤로 가라는 뜻
2번조건은 델타 맵 구성할때 순서를 반시계로 하라고 하는거.

방향
$d$가
$0$인 경우 북쪽,
$1$인 경우 동쪽,
$2$인 경우 남쪽,
$3$인 경우 서쪽을 바라보고 있는 것이다.

1이면 벽, 0이면 청소되지 않음.

위 두개 동작으로 로봇청소기를 구현하면 된다.
시간제한 2초, 맵 크기가 그렇게 크지 않음.
"""

import sys
input = sys.stdin.readline

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
si, sj, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

clean_cnt = 0
stack = [(si, sj)]

while len(stack) != 0:
    i, j = stack.pop()
    # 조건 1 현재 칸이 청소되어 있지 않음.
    if matrix[i][j] == 0:
        matrix[i][j] = 2
        clean_cnt += 1
    side_chk = 0
    # 주변 확인하고 2, 3중 하나 선택하기
    for k in range(4):
        ni = i + delta[k][0]
        nj = j + delta[k][1]

        # 초과하지 않고, 벽이 아니며, 청소되어 있지 않은 칸의 수를 세서
        # 그게 1 이상이라도 있으면 3번, 그게 없으면 2번으로 처리한다.
        if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 0:
            side_chk += 1
            break
    # 청소할 곳이 없음. 2번 로직
    if side_chk == 0:
        bi = i + delta[d][0] * -1
        bj = j + delta[d][1] * -1
        if 0 <= bi < N and 0 <= bj < M and matrix[bi][bj] != 1:
            stack.append((bi, bj))
        else:
            break
    # 청소할 곳이 있음. 3번 로직
    else:
        # 반 시계 방향으로 한바퀴 회전
        d = (d - 1) % 4
        fi = i + delta[d][0]
        fj = j + delta[d][1]
        if 0 <= fi < N and 0 <= fj < M and matrix[fi][fj] == 0:
            stack.append((fi, fj))
        else:
            stack.append((i, j))

print(clean_cnt)


