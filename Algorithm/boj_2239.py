# boj_2239.py
# 스도쿠
"""
그냥 열단위, 행단위, 셀단위로 세트 연산해서 예비숫자 1개만 남으면 픽스하고 pass
아니면 예비슷자 행렬 값 저장하고

더 이상 할게 없어지면 백트래킹?
"""


def cell_check(i, j):
    cell_i = i // 3
    cell_j = j // 3
    t_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    used = set()
    for ii in range(cell_i * 3, cell_i * 3 + 3):
        for jj in range(cell_j * 3, cell_j * 3 + 3):
            if matrix[ii][jj] != 0:
                used.add(matrix[ii][jj])
    return t_nums - used


def row_check(i):
    t_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return t_nums - set(matrix[i])


def col_check(j):
    t_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    n_col = set()
    for i in range(9):
        n_col.add(matrix[i][j])
    return t_nums - n_col


def all_check():
    while True:
        c_cnt = 0
        for i in range(9):
            for j in range(9):
                if matrix[i][j] == 0:
                    cell_result = cell_check(i, j)
                    cell_result &= row_check(i)
                    cell_result &= col_check(j)
                    if len(cell_result) == 1:
                        matrix[i][j] = list(cell_result)[0]
                        c_cnt += 1
                        temp_m[i][j] = 0
                    else:
                        temp_m[i][j] = list(cell_result)
                        temp_m[i][j].sort()
                    if matrix[i][j] == 0 and len(temp_m[i][j]) == 0:
                        return False
        if c_cnt == 0:
            return True


def solving():
    global temp_m
    if all_check() is False:
        return None
    zero_cnt = True
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                zero_cnt = False
                break
        if zero_cnt is False:
            break

    if zero_cnt:
        return matrix
    for ii in range(len(temp_m[i][j])):
        matrix[i][j] = temp_m[i][j][ii]
        a = solving()
        if a:
            return a
        else:
            matrix[i][j] = 0
    return None


nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
matrix = [list(map(int, input().strip())) for _ in range(9)]
temp_m = [[0] * 9 for _ in range(9)]
change = 0

all_check()
result_matrix = solving()

for arr in matrix:
    print("".join(map(str, arr)))
