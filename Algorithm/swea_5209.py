# swea_5209.py
# 백트래킹 공장 문제

"""
제품 수 == 공장 수가 동일하기 때매 특정 공장이 생산할 제품이 픽스되면 다른 공장은 해당 제품을 생산할 수 없다.
가지치기 조건으로 len(arr) == N 이 될 때, 최저 가격을 갱신하게 하고, 중간 가격을 계산하면서 갱신해 가지치기 해서 탐색하면 될듯?
"""


def backT(arr, row, n_val, N):
    global result
    if len(arr) == N:
        result = min(result, n_val)
        return

    if n_val >= result:
        return

    for i in range(N):
        if i not in arr:
            arr.append(i)
            backT(arr, row + 1, n_val + matrix[row][i], N)
            arr.pop()


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 10 ** 9
    backT([], 0, 0, N)
    print(f"#{case} {result}")
