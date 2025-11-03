# swea_4875.py
# 미로

"""
NxN 크기의 미로에서 출발지에서 목적지에 도착하는
경로가 존재하는지 확인하는 프로그램을 작성하시오.
도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.

13101
10101
10101
10101
10021

마지막 2에서 출발해서 0인 통로를 따라 이동하면 3에 도착할 수 있는지 확인하면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가
주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,
계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

완전탐색으로 풀자. N, T 둘다 안크다.

델타 탐색을 통해서 갈 수 있는 영역을 탐지하고
갈 수 있으면 간다. 그리고 방문자에 기록한다.
만약, 델타탐색을 통해서 더 이상 갈 곳이 없다면 -> pop 한다.
이걸 while 로 돌려서 도착지에 도달 하거나, stack 의 길이가 0이 될 때 까지 한다.
"""

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    start_i = 0;  end_i = 0
    start_j = 0;  end_j = 0
    matrix = [list(map(int, input().strip())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start_i = i
                start_j = j
            elif matrix[i][j] == 3:
                end_i = i
                end_j = j

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 스택에 넣을 자료구조 모양
    # (i, j)
    stack = [(start_i, start_j)]
    visits = set()
    success = False
    while len(stack) != 0:
        i, j = stack.pop()
        visits.add((i, j))
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 종료조건
            if ni == end_i and nj == end_j:
                success = True
                break
            # 맵 밖의 영역값이 아니고, 통로도 아니며, 방문자 리스트에도 없다면
            if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 0 and (ni, nj) not in visits:
                stack.append((ni, nj))

    if success:
        print(f"#{case} 1")
    else:
        print(f"#{case} 0")
