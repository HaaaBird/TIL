# swea_4751.py
# 다솔이의 다이아몬드 장식

import pprint
T = int(input())
for case in range(1, T + 1):
    word = input()
    N = len(word)
    matrix = [[0] * (5 * (len(word)-1) + 1) for _ in range(5)]
    cnt = 0
    for idx in range(2, len(matrix[0]), 4):
        matrix[2][idx] = word[cnt]
        cnt += 1

    pprint.pprint(matrix)