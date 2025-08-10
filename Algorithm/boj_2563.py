# boj_2563.py
# 색종이

import sys
input = sys.stdin.readline

matrix = [[0] * 100 for _ in range(100)]
N = int(input())
papers = [tuple(map(int, input().split())) for _ in range(N)]

for paper in papers:
    for i in range(paper[1], paper[1] + 10):
        for j in range(paper[0], paper[0] + 10):
            matrix[i][j] += 1
t_sum = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] != 0:
            t_sum += 1
print(t_sum)