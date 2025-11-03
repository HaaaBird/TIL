# boj_16236.py
# 아기 상어

from collections import deque
from pprint import pprint
import sys

"""
상어는 9번, 나머지는 물고기
이동 거리 가까운 순으로 움직여야 한다. bfs로 거리 측정 해서 간다.
동일한 거리에 물고기가 여러마리면
    가장 위에 있는 물고기, 가장 왼쪽 물고기 쪽으로 간다.

만약 먹을 수 없다면,
    물고기가 없거나
    나 보다 작은 사이즈의 고기가 없다면
종료한다.

크기가 작은 물고기만 먹을 수 있다
크기가 같은 물고기면 그냥 통과해서 지나갈 수 있다.
크기가 더 크면 거긴 못지나간다.

레벨업을 하기 위해서는 자신의 몸 크기만큼의 물고기를 먹어야 한다.
cnt로 관리해서 레벨 업도 시켜야 한다.

일단 매트리스를 받고
물고기 좌표를 따로 뺀다.
 
상어에서 bfs를 돌려서 가장 가까운 물고기를 찾는다.
거기로 순간이동 하고 물고기를 먹는다.
    물고기를 먹었다면 상어의 먹이값을 갱신한다
    현재 몸집과 동일하면 레벨업 시킨다.
"""


def bfs(s_i, s_j):
    queue = deque([(s_i, s_j, 0)])
    visit = {(s_i, s_j)}
    min_dist = 1000
    can_eat = []
    while len(queue) != 0:
        i, j, d = queue.popleft()
        # 만약 물고기를 만났고 상어보다 몸집이 작다면
        if matrix[i][j] != 0 and matrix[i][j] < shark[0] and matrix[i][j] != 9 and d <= min_dist:
            min_dist = d
            can_eat.append((i, j, d))
        # 가지치지 조건. 이미 갱신된 값 보다 더 멀리 있는 놈들은 찾을 필요가 없다.
        if d >= min_dist:
            continue
        # 가지치기 조건도 통과했다면 델타 탐색
        for k in range(4):
            ni = i + delta[k][0]
            nj = j + delta[k][1]
            if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] <= shark[0] and (ni, nj) not in visit:
                queue.append((ni, nj, d + 1))
                visit.add((ni, nj))
    if len(can_eat) != 0:
        can_eat.sort(key=lambda x: (x[0], x[1]))
        return can_eat[0]
    else:
        return -1



delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 우 하 좌
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 상어 찾기
shark = [2, 0, 0, 0]  # 몸집, 먹은 먹이, i, j
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            shark[2] = i
            shark[3] = j
            break

# 상어한테 가까운 물고기 찾기
time_cnt = 0
while True:
    find_fish = bfs(shark[2], shark[3])
    if find_fish == -1:
        print(time_cnt)
        break
    else:
        # 갈 물고기가 있으니 물고기한테 가기.
        matrix[shark[2]][shark[3]] = 0
        matrix[find_fish[0]][find_fish[1]] = 9
        time_cnt += find_fish[2]
        # 상어 위치 갱신
        shark[2] = find_fish[0]
        shark[3] = find_fish[1]
        # 상어 먹이 먹기
        shark[1] += 1
        if shark[1] == shark[0]: # 진화 조건 도달 했다면
            # 진화시키고 초기화
            shark[0] += 1
            shark[1] = 0




