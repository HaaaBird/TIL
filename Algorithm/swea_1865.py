# swea_1865.py
# 동철이의 일 분배
import sys
sys.stdin = open("input.txt", "r")

def backT(arr, n_p, N):
    global result
    if len(arr) == N:
        result = max(result, n_p)
    if n_p <= result:
        return
    for i in range(N):
        if i not in arr and (matrix[len(arr)][i] > 0):
            arr.append(i)
            k = len(arr) - 1
            backT(arr, n_p * (matrix[k][i] * 0.01), N)
            arr.pop()

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    backT([], 100, N)
    print(f"#{case} {round(result, 6):.6f}")
