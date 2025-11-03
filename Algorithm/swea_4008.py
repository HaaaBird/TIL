# swea_4008.py
# 숫자 만들기

"""

"""


def backT(op_arr, in_op_arr):
    global min_result, max_result
    if sum(op_arr) == 0:
        result = num_list[0]
        for j in range(N - 1):
            if in_op_arr[j] == 0:
                result += num_list[j + 1]
            elif in_op_arr[j] == 1:
                result -= num_list[j + 1]
            elif in_op_arr[j] == 2:
                result *= num_list[j + 1]
            elif in_op_arr[j] == 3:
                result = int(result / num_list[j + 1])
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    for i in range(4):
        if i == 0:
            if op_arr[i] > 0:
                in_op_arr.append(i)
            else:
                continue
        elif i == 1:
            if op_arr[i] > 0:
                in_op_arr.append(i)
            else:
                continue
        elif i == 2:
            if op_arr[i] > 0:
                in_op_arr.append(i)
            else:
                continue
        elif i == 3:
            if op_arr[i] > 0:
                in_op_arr.append(i)
            else:
                continue
        op_arr[i] -= 1
        backT(op_arr, in_op_arr)
        op_arr[i] += 1
        in_op_arr.pop()


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    op_lst = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_result = -10 ** 9
    min_result = 10 ** 9
    backT(op_lst, [])
    print(f"#{case} {max_result - min_result}")
