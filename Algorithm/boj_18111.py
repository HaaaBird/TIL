# boj_18111.py
# 마인크래프트

"""
문제

lvalue는 세로 N, 가로 M 크기의 집터를 골랐다.
집터 맨 왼쪽 위의 좌표는 (0, 0)이다.

우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다.

우리는 다음과 같은 두 종류의 작업을 할 수 있다.

1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다.
밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다.
‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.

단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며,
집터 바깥에서 블록을 가져올 수 없다. 또한,
작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다.
땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

입력
첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107)

둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다. (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.

256까지의 높이를 보면서 탐색해야 함.

3 3 1
8 5 7
6 8 4
1 9 5

값을 빈도 배열로 저장해서 빠른 계산을 구현.
시도할 높이 최대값: (깔려있는 모든 블럭 + 인벤토리) // 칸의 총 수(N * M) 가 최대 높이고
여기서 한칸씩 내려가면서 시간 측정
"""
import sys
input = sys.stdin.readline

N, M, inventory = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cnt_list = [0] * 257
all_block_cnt = 0
for i in range(N):
    for j in range(M):
        all_block_cnt += matrix[i][j]
        cnt_list[matrix[i][j]] += 1

search_range = int((all_block_cnt + inventory) / (N * M))

result_time = 100000000000000000000000
result_height = 1000000000000000000000
for height in range(0, search_range + 1):
    n_total_time = 0
    for idx in range(len(cnt_list)):
        if height > idx: # 높여야 하는 경우
            n_total_time += (height - idx) * cnt_list[idx]
        elif height < idx: # 깎아야 하는 경우
            n_total_time += (idx - height) * cnt_list[idx] * 2

    if result_time >= n_total_time:
        if result_time == n_total_time and result_height < height:
            result_height = height
        else:
            result_height = height
            result_time = n_total_time
print(result_time, result_height)