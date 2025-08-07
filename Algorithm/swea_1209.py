# swea_1209.py
# sum 문제

import sys
sys.stdin = open("input.txt", "r")

for case in range(10):
    case_num = int(input())
    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))
    sum_1 = 0 # 대각 정방향
    sum_2 = 0 # 대각 역방향
    sum_3 = 0 # 행 방향
    sum_4 = 0 # 열 방향
    for i in range(100):
        sum_1 += matrix[i][i]
        sum_2 += matrix[i][100 - 1 - i]
        sum_3_sub = 0
        sum_4_sub = 0
        for j in range(100):
            sum_3_sub += matrix[i][j]
            sum_4_sub += matrix[j][i]
        if sum_3 < sum_3_sub:
            sum_3 = sum_3_sub
        if sum_4 < sum_4_sub:
            sum_4 = sum_4_sub

    print(f"#{case_num} {max(sum_1, sum_2, sum_3, sum_4)}")