# swea_1953.py
# 탈주범 검거

import pprint

"""
그냥 전형적인 bfs 풀이 문제
각 노드 순회하면서 갈 수 있는 곳을 배열에 저장해서 그린다
    이 때 주의할 것은 반대편 파이프로 갈 수 있는지 확인한다.
    델타 쓴다.

bfs를 풀 때, 결국 max level에 도달하면 더 이상 내려가지 않는다. -> 검색 큐에 자식을 추가하지 말라.

먼저 배열 순회하면서 tree 구성하는 코드 먼저 구현
수를 보고, 0이 아니면 delta_dict의 값을 확인해서 delta map을 잡아온다.

그러다,matrix[ni][nj] != 0:
matrix[ni][nj]의 델타를 확인해서 ni, i,j 가 상대 델타맵에도 잡히는지 확인한다.
잡히면 tree에 추가한다.
tree 자료 형태는
tree = {(i,j):[[ni, nj],[ni, nj],[ni, nj],[ni, nj]]}
"""
delta_dict = {
    1: [[0, 1, 0, -1], [1, 0, -1, 0]],  # 동 남 서 북
    2: [[-1, 1], [0, 0]],  # 상 하
    3: [[0, 0], [-1, 1]],  # 좌 우
    4: [[-1, 0], [0, 1]],  # 상 우
    5: [[1, 0], [0, 1]],  # 하 우
    6: [[1, 0], [0, -1]],  # 하 좌
    7: [[-1, 0], [0, -1]]  # 상 좌
}


def BFS(s_i, s_j, tree, max_lvl):
    queue = [(s_i, s_j, 1)]
    visits = set()
    idx = 0

    while idx < len(queue):
        ni, nj, lvl = queue[idx]
        idx += 1
        if (ni, nj) not in visits:
            visits.add((ni, nj))
            child = tree[(ni, nj)]
            if lvl != max_lvl:
                for ch in range(len(child) - 1, -1, -1):
                    ci = child[ch][0]
                    cj = child[ch][1]
                    queue.append((ci, cj, lvl + 1))
    return len(visits)


T = int(input())
for case in range(1, T + 1):
    # 가로크기, 세로크기, 맨홀 가로, 세로, 경과시간
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    tree = {}
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                now_delta = delta_dict[matrix[i][j]]
                di = now_delta[0]
                dj = now_delta[1]
                for c in range(len(di)):
                    ni = i + di[c]
                    nj = j + dj[c]
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] != 0:
                        # 상대 델타 맵도 검사해봐야 한다.
                        side_delta = delta_dict[matrix[ni][nj]]
                        sdi = side_delta[0]
                        sdj = side_delta[1]
                        for sc in range(len(sdi)):
                            sni = ni + sdi[sc]
                            snj = nj + sdj[sc]
                            if 0 <= sni < N and 0 <= snj < M and sni == i and snj == j:
                                if tree.get((i, j)) is not None:
                                    tree[(i, j)].append([ni, nj])
                                else:
                                    tree.update({(i, j): [[ni, nj]]})
    result = BFS(R, C, tree, L)
    print(f"#{case} {result}")
