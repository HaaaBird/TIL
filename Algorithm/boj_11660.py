# boj_11660.py
# 누적합

"""
2차원 배열이지만 행 단위로 누적합 구해서 하면 될듯?
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    temp = list(map(int, input().split()))
    sum_arr = [0] * N
    for i in range(N):
        if i == 0:
            sum_arr[i] = temp[i]
        else:
            sum_arr[i] = sum_arr[i-1] + temp[i]
    matrix.append(sum_arr)
order_list = [list(map(int, input().split())) for _ in range(M)]

for order in order_list:
    n_sum = 0
    for ni in range(order[0]-1, order[2]):
        if order[1] == 1:
            n_sum += matrix[ni][order[3]-1]
        else:
            n_sum += matrix[ni][order[3]-1] - matrix[ni][order[1]-2]
    print(n_sum)
