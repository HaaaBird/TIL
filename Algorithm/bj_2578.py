def horizontal_check(array):
    return sum(1 for row in array if sum(row) == 0)

def vertical_check(array):
    bingo_count = 0
    for x in range(5):
        col_sum = 0
        for y in range(5):
            col_sum += array[y][x]  # ✅ col 고정
        if col_sum == 0:
            bingo_count += 1
    return bingo_count

def cross_check(array):
    bingo_count = 0
    # left -> right
    if sum(array[i][i] for i in range(5)) == 0:
        bingo_count += 1
    # right -> left
    if sum(array[i][4 - i] for i in range(5)) == 0:
        bingo_count += 1
    return bingo_count

def total_check(array):
    total_bingo = horizontal_check(array) + vertical_check(array) + cross_check(array)
    return total_bingo >= 3

def find_num(array, call_num):
    for y in range(5):
        for x in range(5):
            if array[y][x] == call_num:
                array[y][x] = 0

bingo_board = [list(map(int, input().split())) for _ in range(5)]
call_array = [list(map(int, input().split())) for _ in range(5)]

mc_call_count = 0
for i in range(5):
    for k in range(5):
        find_num(bingo_board, call_array[i][k])
        mc_call_count += 1
        if total_check(bingo_board):
            print(mc_call_count)
            exit()
