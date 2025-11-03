# swea_11315.py
# 오목 판정
def five_check():
    directions = [[0, 1], [-1, 0], [1, 1], [1, -1]] # 오른쪽, 아랫방향 우하 좌하

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(str, input().strip())) for _ in range(N)]
    