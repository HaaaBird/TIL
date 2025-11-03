# boj_2566.py
# 최댓값


matrix = [list(map(int, input().split())) for _ in range(9)]

max_i = None
max_j = None
max_val = -1
for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_i = i + 1
            max_j = j + 1


print(max_val)
print(max_i, max_j)