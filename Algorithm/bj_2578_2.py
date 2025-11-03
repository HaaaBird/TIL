def vertical_check(array):
    bingo_count = 0
    for row in array:
        if sum(row) == 0:
            bingo_count += 1
    return bingo_count

def horizontal_check(array):
    bingo_count = 0
    col_sum = 0
    for x in range(len(array)):
        col_sum = 0
        for y in range(len(array)):
            col_sum += array[y][x]
        if col_sum == 0:
            bingo_count += 1
    return bingo_count

def cross_check(array):
    bingo_count = 0
    col_sum = [0,0]
    for i in range(len(array)):
        col_sum[0] += array[i][i]
        col_sum[1] += array[i][4-i]
    return col_sum.count(0)

def all_check(array):
    return vertical_check(array) + horizontal_check(array) + cross_check(array)


def number_remover(array, number):
    global bingo_size
    for y in range(bingo_size):
        for x in range(bingo_size):
            if array[y][x] == number:
                array[y][x] = 0


if __name__ == "__main__":
    global bingo_size
    bingo_size = 5
    bingo_array = []
    number_call_array = []

    # get bingo arry
    for i in range(bingo_size):
        bingo_array.append(list(map(int, input().split())))
    # get number
    for i in range(bingo_size):
        number_call_array = number_call_array + list(map(int, input().split()))
    # remove number
    count = 0
    for num in number_call_array:
        number_remover(bingo_array, num)
        count += 1
        if all_check(bingo_array) >= 3:
            print(count)
            break