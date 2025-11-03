from pprint import pprint
from heapq import heappop, heappush


def dijkstra_shortest_path(map_grid, start, end):
    rows, cols = len(map_grid), len(map_grid[0])
    # 거리 정보 저장 배열 (초기엔 무한대로 설정)
    distance = [[float('inf')] * cols for _ in range(rows)]
    distance[start[0]][start[1]] = 0
    # 경로 추적용 배열
    previous = [[None] * cols for _ in range(rows)]

    # 우선순위 큐 (거리, 위치)
    heap = [(0, start)]

    # 방향: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        dist, (x, y) = heappop(heap)

        # 목적지에 도달하면 종료
        if (x, y) == end:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 맵 범위 내 & 벽이 아닐 경우
            if 0 <= nx < rows and 0 <= ny < cols and map_grid[nx][ny] == "G":
                new_dist = dist + 1  # 모든 가중치는 1

                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    previous[nx][ny] = (x, y)
                    heappush(heap, (new_dist, (nx, ny)))

    # 목적지에 도달할 수 없는 경우
    if distance[end[0]][end[1]] == float('inf'):
        return None, -1

    # 경로 복원
    path = []
    current = end
    while current:
        path.append(current)
        current = previous[current[0]][current[1]]
    path.reverse()

    return path, distance[end[0]][end[1]]


def find_area(ti, tj):
    for r in range(1, 4):
        for k in range(4):
            ni = ti + DIRS[k][0]
            nj = tj + DIRS[k][1]
            if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == "G":
                matrix[ni][nj] = "ST"


def find_positions(grid, start_mark, goal_mark):
    rows, cols = len(grid), len(grid[0])
    start = goal = None

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == start_mark:
                start = (row, col)

            elif grid[row][col] == goal_mark:
                goal = (row, col)

    return start[0], start[1], goal[0], goal[1]

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
WALL_SYMBOL = 'R'
total_t = 6
for _ in range(total_t):
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tc = int(input())
    N = int(input())
    matrix = [list(map(str, input().strip())) for _ in range(N)]

    si, sj, ti, tj = find_positions(matrix, "M", "X")


    print(si, sj, ti, tj)
    find_area(ti, tj)
    move_result, dists = dijkstra_shortest_path(matrix,(si, sj),(ti, tj))

    print(move_result)
    pprint(move_result)
    print(dists)
