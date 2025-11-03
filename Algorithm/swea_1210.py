# swea_1210.py
# 사다리타기
import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    case = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    N = 100
    now_i = 99
    now_j = matrix[now_i].index(2)


    while now_i > 0:
        if now_j > 0 and matrix[now_i][now_j -1] == 1:
            while now_j > 0 and matrix[now_i][now_j -1] == 1:
                now_j -= 1
            now_i -= 1
            continue
        elif now_j < N - 1 and matrix[now_i][now_j + 1] == 1:
            while now_j < N - 1 and matrix[now_i][now_j + 1] == 1:
                now_j += 1
            now_i -= 1
            continue
        elif now_i > 0 and matrix[now_i-1][now_j] == 1:
            now_i -= 1
            continue
        else:
            break

    print(now_i, now_j)

