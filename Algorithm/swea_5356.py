# swea_5356.py
# 의석이의 세로로 말해요
import sys

input = sys.stdin.readline

T = int(input())
for case in range(1, T + 1):
    matrix = [list(map(str, input().strip())) for _ in range(5)]
    max_len = max(len(row) for row in matrix)
    word = []

    for j in range(max_len):
        for i in range(5):
            if len(matrix[i])-1 >= j:
                word.append(matrix[i][j])
    print(f"#{case} {''.join(word)}")
