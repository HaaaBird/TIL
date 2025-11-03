# swea_1979.py
# 어디에 단어가 들어갈 수 있을까?

# 열/행 단위로 읽어서 연속공간이 k 만큼 있는지 확인
# 딱 맞는 연속공간이 있으면 +1
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    possible_cnt = 0
    # 행에 공간이 있는지; 확인
    for arr in matrix:
        max_size = []
        cur_size = 0
        for val in arr:
            if val == 1:
                cur_size += 1
            else:
                if cur_size != 0:
                    max_size.append(cur_size)
                cur_size = 0
        max_size.append(cur_size)
        possible_cnt += max_size.count(K)
    for j in range(N):
        max_size = []
        cur_size = 0
        for i in range(N):
            if matrix[i][j] == 1:
                cur_size += 1
            else:
                if cur_size != 0:
                    max_size.append(cur_size)
                cur_size = 0
        max_size.append(cur_size)
        possible_cnt += max_size.count(K)

    print(f"#{case} {possible_cnt}")
