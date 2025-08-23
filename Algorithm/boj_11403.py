# boj_11403.py
# 경로 찾기

"""
문제
가중치 없는 방향 그래프 G가 주어졌을 때,
모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다.
둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다.
i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고,
0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

출력
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다.
정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.

그냥 1번부터 시작해서 bfs로 탐색
탐색해서 도달 가능하면 인접행렬 결과 출력 그래프에 값을 1로 변경
"""
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            queue = [j]
            visit[i][j] = 1
            head = 0
            while head < len(queue):
                now_j = queue[head]
                head += 1
                for idx in range(N):
                    if arr[now_j][idx] == 1 and visit[i][idx] != 1:
                        queue.append(idx)
                        visit[i][idx] = 1

for i in range(N):
    print(" ".join(map(str, visit[i])))