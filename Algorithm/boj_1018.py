# boj_1018.py
# 체스판 다시 칠하기

# 8 x 8 배열을 잘라서 만든다
# 첫 번째 iter일 경우 t_color를 첫 번째 컬러로 잡아버린다.
# 해당 줄의 8개를 모두 확인하며 칠할 필요가 있으면 칠한다.
# 다음 줄은 t_color 반대로 잡고 칠할 건 칠하고 칠한 수량을 더한다.
# 해당 칠을 가장 덜 해도 되는 8x8을 찾는다.

import sys
input = sys.stdin.readline
color_arr = [["B","W"], ["W","B"]] # 0이 검정, 1이 흰색


N, M = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(N)]
min_cnt = 999999

for i in range(0, N-7):
    for j in range(0, M-7):
        for color_set in color_arr:
            paint_cnt = 0
            for ii in range(i, i+8):
                for jj in range(j, j+8):
                    if matrix[ii][jj] != color_set[(ii+jj) % 2]:
                        paint_cnt += 1
            min_cnt = min(min_cnt, paint_cnt)
print(min_cnt)