def horizontal_check(array):
    bingo_count = 0
    for row in array:
        if sum(row) == 0:
            bingo_count += 1
    return bingo_count

def vertical_check(array):
    bingo_count = 0
    for x in range(5):
        now_col = 0
        for y in range(5):
            now_col += array[x][y]
        if now_col == 0:
            bingo_count += 1
    return bingo_count

def cross_check(array):
    #left -> right 
    bingo_count = 0
    now_sum = 0
    for i in range(5):
        now_sum += array[i][i]
    if now_sum == 0: bingo_count += 1 
    # right -> left
    now_sum = 0
    for i in reversed(range(5)):
        x = 4 - i
        now_sum += array[i][x]
    if now_sum == 0: bingo_count += 1 
    
    return bingo_count

def total_check(array):
    total_bingo = 0
    total_bingo += horizontal_check(array)
    total_bingo += vertical_check(array)
    total_bingo += cross_check(array)
    if total_bingo >= 3:
        return True
    else:
        return False

def find_num(array, call_num):
    for y in range(len(array)):
        for x in range(len(array)):
            if array[y][x] == call_num: array[y][x] = 0



# get Bingo Sheet
bingo_board = []

for i in range(5):
    bingo_board.append(list(map(int, input().split())))

call_array = []
for i in range(5):
    call_array.append(list(map(int, input().split())))
is_end = False
mc_call_count = 0
for i in range(5):
    for k in range(5):
        find_num(bingo_board, call_array[i][k])
        mc_call_count += 1
        is_end = total_check(bingo_board)
        if is_end:
            print(mc_call_count)
            break
    if is_end:
        break