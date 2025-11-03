# swea_2819.py
# 격자판의 숫자 이어 붙이기
"""
4x4인데다 시간 8초면 완탐 가능
"""
from collections import deque

def backT(arr, si, sj):
    global result
    if len(arr) == 7:
        if "".join(map(str, arr)) not in result:
            result.add("".join(map(str, arr)))
        return

    for k in range(4):
        ni = si + delta[k][0]
        nj = sj + delta[k][1]
        if 0 <= ni < 4 and 0 <= nj < 4:
            arr.append(matrix[ni][nj])
            backT(arr, ni, nj)
            arr.pop()


delta = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동서남북
T = int(input())
for case in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            backT([matrix[i][j]], i, j)

    print(f"#{case} {len(result)}")