# boj_1987.py
# 알파벳


from collections import deque


def backT(i, j, dist):
    global result
    result = max(result, dist)
    pass_flag = False
    for k in range(4):
        ni = i + delta[k][0]
        nj = j + delta[k][1]
        if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] not in visit:
            pass_flag = True
            visit.add(matrix[ni][nj])
            backT(ni, nj, dist + 1)
            visit.remove(matrix[ni][nj])
    if pass_flag is False:
        return


R, C = map(int, input().split())
matrix = [list(input().strip()) for _ in range(R)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0
visit = {matrix[0][0]}
backT(0, 0, 1)

print(result)
