# boj_17144.py
# 미세먼지

"""
공기청정기 위치를 찾는다.
그 다음 초 만큼 for 문 반복 돌린다.

먼저 미세먼지 확산을 처리한다.
4개방향 델타를 순회하며 순회 가능한 셀을 찾는다.
    공기청정기가 있거나, 범위 외라면 추가 안한다.
    추가 가능하다면 해당 칸에 20% 만큼 뿌리고 카운터 증분
for 문이 끝나고 나면 카운터 증분 * 20% 한다.

바람을 불게 한다.
어차피 첫 줄에만 있으니까 for 문 순회하면서 -1을 처음 만난 좌표를 찍어둔다.
델타를 2개 돌린다.

"""
import sys
input = sys.stdin.readline

delta_1 = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 윗쪽 방향 델타
delta_2 = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 아랫쪽 방향 델타

R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]
air_cleaner = None
for i in range(R):
    if matrix[i][0] == -1:
        air_cleaner = [i, i+1]
        break

for _ in range(T):
    # 미세먼지 확산 로직
    add_dust = []
    for i in range(R):
        for j in range(C):
            if matrix[i][j] != -1 and matrix[i][j] != 0:
                cnt = 0
                for k in range(4):
                    ni = i + delta_1[k][0]
                    nj = j + delta_1[k][1]
                    if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] != -1:
                        add_dust.append((ni, nj, matrix[i][j] // 5))
                        cnt += 1
                matrix[i][j] -= (matrix[i][j] // 5) * cnt
    for di, dj, dv in add_dust:
        matrix[di][dj] += dv

    # 공기청정기 동작

    # 윗쪽방향 시작위치
    nd_1 = 0
    nd_2 = 0
    ci_1 = air_cleaner[0]
    cj_1 = 0
    ci_2 = air_cleaner[1]
    cj_2 = 0
    temp = 0
    temp_2 = 0
    while True:
        # 윗쪽방향
        ni = ci_1 + delta_1[nd_1][0]
        nj = cj_1 + delta_1[nd_1][1]
        if 0 <= ni < R and 0 <= nj < C:
            if matrix[ni][nj] == -1: # 공기청정기를 만나면
                break
            else:
                n_temp = matrix[ni][nj]
                matrix[ni][nj] = temp
                temp = n_temp
                ci_1 = ni
                cj_1 = nj
        else:
            nd_1 += 1
    while True:
        # 아랫방향
        ni = ci_2 + delta_2[nd_2][0]
        nj = cj_2 + delta_2[nd_2][1]
        if 0 <= ni < R and 0 <= nj < C:
            if matrix[ni][nj] == -1:  # 공기청정기를 만나면
                break
            else:
                n_temp = matrix[ni][nj]
                matrix[ni][nj] = temp_2
                temp_2 = n_temp
                ci_2 = ni
                cj_2 = nj
        else:
            nd_2 += 1
result = 2
for i in range(R):
    for j in range(C):
        result += matrix[i][j]

print(result)




