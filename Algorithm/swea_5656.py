# swea_5656.py
# 벽돌 깨기

import copy

"""
받아온 행렬 90도 꺾어서 해야할듯?
중력 처리 로직이 행 방향인게 훨씬 더 쉬움.
"""


def backT(in_matrix, kill_cnt, n):
    global max_score
    if n == 0:
        max_score = max(max_score, kill_cnt)
        return
    for ai in range(W):
        cp_matrix = [col[:] for col in in_matrix]
        stack = []
        for aj in range(H):  # 첫 번째로 도달하는 블럭 찾기
            if cp_matrix[ai][aj] == 0:
                pass
            else:
                stack.append((ai, aj, cp_matrix[ai][aj]))
                break
        now_kill = 0
        while len(stack) != 0:
            i, j, p = stack.pop()
            for r in range(p):
                for k in range(4):
                    ni = i + (delta[k][0] * r)
                    nj = j + (delta[k][1] * r)
                    if 0 <= ni < W and 0 <= nj < H and cp_matrix[ni][nj] != 0:
                        if cp_matrix[ni][nj] > 1:
                            stack.append((ni, nj, cp_matrix[ni][nj]))
                        cp_matrix[ni][nj] = 0
                        now_kill += 1

        # 중력 처리
        nxt_matrix = []
        for ii in range(W):
            new_arr = []
            for jj in range(H):
                if cp_matrix[ii][jj] != 0:
                    new_arr.append(cp_matrix[ii][jj])
            n_len = len(new_arr)
            new_arr = [0] * (H - n_len) + new_arr
            nxt_matrix.append(new_arr)
        backT(nxt_matrix, kill_cnt + now_kill, n - 1)


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

T = int(input())
for case in range(1, T + 1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    n_matrix = []
    max_score = 0
    block_cnt = 0
    for j in range(W):
        new_row = []
        for i in range(H):
            new_row.append(matrix[i][j])
            if matrix[i][j] != 0:
                block_cnt += 1
        n_matrix.append(new_row)

    backT(n_matrix, 0, N)
    print(f"#{case} {block_cnt - max_score}")
