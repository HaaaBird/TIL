# boj_2239.py
# 스도쿠
"""


전체 탐색을 하며 값이 0인 곳을 찾는다.
거기에 1~9까지 숫자를 넣어보며 확인을 한다.

1. 숫자를 넣어보고 행렬 단위 델타탐색을 통해 동일한 숫자가 있는지 확인한다.
2. i // 3 j // 3연산 통해서 해당 박스 위치를 추론하고, 박스 내에 동일한 숫자가 있는지 확인한다.

위 두개 검사를 pass 하면 숫자를 넣는다? 아니지.
값이 하나라면 값을 넣는다.
두개라면 예비숫자.
스도쿠 맵이랑 동일한 크기의 매트릭스를 만들어서, 각 셀 별로 set값으로 저장해야겠다.

매트릭스 순회하면서 예비 숫자중 하나를 넣어본다. 넣을때 마다 재귀 써서 스택에 재귀 쌓으면서 한다.
그러다 실패하면 뒤 돌아가게 구성
"""

import pprint


def cell_check(matrix, note, i, j, target_num):
    answer_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # 행 방향 후보 정리
    for jj in range(9):
        if matrix[i][jj] == target_num:
            return False
    # 열 방향 후보 정리
    for ii in range(9):
        if matrix[ii][j] == target_num:
            return False
    for bi in range(3):
        for bj in range(3):
            bbi = bi + ((i // 3) * 3)
            bbj = bj + ((j // 3) * 3)
            if matrix[bbi][bbj] == target_num:
                return False
    return True


def all_cell_check(matrix, note):
    answer_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    while True:
        change_flag = False
        for i in range(9):
            for j in range(9):
                if matrix[i][j] != 0:
                    continue
                candidate_set = set()
                # 행 방향 후보 정리
                for jj in range(9):
                    if matrix[i][jj] != 0:
                        candidate_set.add(matrix[i][jj])
                # 열 방향 후보 정리
                for ii in range(9):
                    if matrix[ii][j] != 0:
                        candidate_set.add(matrix[ii][j])
                for bi in range(3):
                    for bj in range(3):
                        bbi = bi + ((i // 3) * 3)
                        bbj = bj + ((j // 3) * 3)
                        if matrix[bbi][bbj] != 0:
                            candidate_set.add(matrix[bbi][bbj])
                now_candidate = answer_set - candidate_set
                if len(now_candidate) == 1:
                    matrix[i][j] = now_candidate.pop()
                    note[i][j] = 0
                    change_flag = True
                else:
                    note[i][j] = list(now_candidate)
        if change_flag is False:
            break

def zero_check(matrix):
    cnt = 0
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                cnt += 1
    return cnt

def insert_new_num(matrix, i, j):
    for ii in range(i, 9):
        for jj in range(j, 9):
            if matrix[ii][jj] == 0:

    pass

matrix = [list(map(int, input().strip())) for _ in range(9)]
note = [[0] * 9 for _ in range(9)]
all_cell_check(matrix, note)

if zero_check(matrix) == 0:
    for arr in matrix:
        print("".join(map(str, arr)))
else:


