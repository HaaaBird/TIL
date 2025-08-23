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

제일 간단하고 이미 알고 있는 방법.
그래프 만들어서 bfs 로 풀기.

그래프 만들기

1. 전역 탐색하며 0이 아닌 곳 찾기.
2. 0이 아니라면, 해당하는 숫자 델타 써서 반대편 탐색
3. 반대편이 0이 아니라면, 해당 통로가 이동 가능한지 다시 확인.
3.1 해당 통로가 이동 가능한지?
4. 이후 시작 위치 기준으로 bfs탐색해서 가능한 영역의 수 도출 및 출력
"""

def BFS(tree, s_i, s_j, max_lvl):
    queue = [(s_i, s_j)]
    result_cnt = 0
    level = 0
    visit = set()
    while len(queue) != 0:
        ni, nj = queue.pop(0)
        visit.add((ni, nj))
        result_cnt += 1
        if max_lvl != level:
            if tree.get((ni, nj)) is not None:
                for i in range(len(tree[(ni, nj)])):
                    if tree[(ni, nj)][i] in visit:
                        pass
                    else:
                        queue.append(tree[(ni, nj)][i])
                level += 1
    return result_cnt
pipe_dict = {
    1:[[-1, 0], [1, 0], [0, -1], [0, 1]],
    2:[[-1, 0], [1, 0]],
    3:[[0, -1], [0, 1]],
    4:[[-1, 0], [0, 1]],
    5:[[1, 0], [0, 1]],
    6:[[1, 0], [0, -1]],
    7:[[-1, 0], [0, -1]]
}
T = int(input())
for case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    tree = {}
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                ni = i
                nj = j
                for k in range(len(pipe_dict[matrix[i][j]])):
                    di = pipe_dict[matrix[i][j]][k][0]
                    dj = pipe_dict[matrix[i][j]][k][1]
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if matrix[ni][nj] != 0:
                            if [-1 * di, -1 * dj] in pipe_dict[matrix[ni][nj]]:
                                if tree.get((i, j)) is None:
                                    tree.update({(i, j):[(ni, nj)]})
                                else:
                                    tree[(i,j)].append((ni, nj))
    result = BFS(tree, R, C, L)
    print(f"#{case} {result}")