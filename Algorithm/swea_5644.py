# swea_5644.py
# 무선 충전

"""

시간 넉넉하다 완탐 쌉가능
빈 배열 선언해두고
충전기 위치 가지고 델터 돌려서 충전 범위에 따른 제공 가능량을 집어넣는다
겹쳐도 append 해서 정렬해버린다.
어차피 적다. 만약 겹치면 sort 써서 내림차순 하자

사용자 동선 가지고 계산할 것은

1. 혼자있는데 충전기가 없다
pass
2. 혼자있는데 충전기가 하나 있다
충전량 더하기
3. 혼자있는데 충전기가 복수다
이 중에 제일 좋은 충전량을 더하기

4. 둘이있는데 없다
pass

5. 둘이있는데 충전기가 하나다.
n빵이니까 충전기 1개 양만큼 충전량 더한다

6. 둘이있는데 충전기가 복수다
충전기 내림차순 2개를 충전량만큼 더한다

충전기는 델타를 2개 돌린다
1. 값이 1일때 쓰는 델타

"""
from pprint import pprint
delta_1 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
delta_2 = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

T = int(input())
for case in range(1, T + 1):
    M, A = map(int, input().split())
    user_1 = list(map(int, input().split()))
    user_2 = list(map(int, input().split()))

    charger_list = [list(map(int, input().split())) for _ in range(A)]
    matrix = [[[] for _ in range(10)] for _ in range(10)]

    for x, y, c, p in charger_list:
        x -= 1
        y -= 1
        matrix[y][x].append(p)
        for i in range(1, c+1):
            if i == 1:
                for k in range(4):
                    ni = y + (delta_1[k][0] * i)
                    nj = x + (delta_1[k][1] * i)
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        matrix[ni][nj].append(p)
            else:
                for k in range(4):
                    ni = y + (delta_1[k][0] * i)
                    nj = x + (delta_1[k][1] * i)
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        matrix[ni][nj].append(p)
                for k in range(4):
                    ni = y + (delta_2[k][0] * (i - 1))
                    nj = x + (delta_2[k][1] * (i - 1))
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        matrix[ni][nj].append(p)
    pprint(matrix)


