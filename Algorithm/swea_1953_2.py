# swea_1953_2.py
# 탈주범 검거

"""
탈주범은 1시간당 1의 거리를 이동 가능
구조물은 7가지

1. 시간 제한 : 최대 50개 테이트 케이스를 모두 통과하는데, C/C++/Java 모두 1초
2. 지하 터널 지도의 세로 크기 N, 가로 크기 M은 각각 5 이상 50 이하이다. (5 ≤ N, M ≤ 50)
3. 맨홀 뚜껑의 세로 위치 R 은 0 이상 N-1이하이고 가로 위치 C 는 0 이상 M-1이하이다. (0 ≤ R ≤ N-1, 0 ≤ C ≤ M-1)
4. 탈출 후 소요된 시간 L은 1 이상 20 이하이다. (1 ≤ L ≤ 20)
5. 지하 터널 지도에는 반드시 1개 이상의 터널이 있음이 보장된다.
6. 맨홀 뚜껑은 항상 터널이 있는 위치에 존재한다.

갈 수 있는 터널에 대해서 delta 구성해두고
터널 만나면 델타탐색. 이 때 반대편 통행 가능한지 확인 필요함.

BFS 써서 시간값 만큼 탐색
"""

from collections import deque

delta = {
    1:[(-1, 0), (1, 0), (0, -1), (0, 1)], 2:[(-1, 0), (1, 0)], 3:[(0, -1), (0, 1)],
    4:[(-1, 0), (0, 1)], 5:[(1, 0), (0, 1)], 6:[(1, 0), (0, -1)], 7:[(-1, 0), (0, -1)]
}

def BFS(R, C, L, ML):
    queue = deque([(R, C, L)])
    visit = {(R, C)}
    while len(queue) != 0:
        i, j, l = queue.popleft()
        d = matrix[i][j]
        for k in range(len(delta[d])):
            ni = i + delta[d][k][0]
            nj = j + delta[d][k][1]
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] != 0 and (ni, nj) not in visit and l+1 < ML:
                if (delta[d][k][0] * -1, delta[d][k][1] * -1) in delta[matrix[ni][nj]]:
                    visit.add((ni, nj))
                    queue.append((ni, nj, l + 1))
    return len(visit)

T = int(input())
for case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = BFS(R, C, 0, L)
    print(f"#{case} {result}")
