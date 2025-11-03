# swea_2105.py
# 디저트 카페

"""
백트래킹으로 풀어 본다면

for i in range(2) # 지금 방향대로 가거나, 방향 한번 바꾸거나
"""

delta = [(1, -1), (1, 1), (-1, 1), (-1, -1)]


def move(i, j, d, visited, si, sj, moving):
    global result, first_move
    if i == si and j == sj and len(visited) != 0:
        if moving[0] == moving[2] and moving[1] == moving[3]:
            if len(visited) == 32:
                print(1)
            result = max(result, len(visited))
        return

    for k in range(2):
        d = (d + k) % 4
        ni = i + delta[d][0]
        nj = j + delta[d][1]
        if 0 <= ni < N and 0 <= nj < N and ni >= si:
            if matrix[ni][nj] not in visited:
                moving[d] += 1
                move(ni, nj, d, visited + [matrix[ni][nj]], si, sj, moving)
                moving[d] -= 1
            else:
                return


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    first_move = True

    for i in range(N - 2):
        for j in range(1, N - 1):
            si = i + delta[0][0]
            sj = j + delta[0][1]
            move(si, sj, 0, [matrix[si][sj]], i, j, [1,0,0,0])
    print(f"#{case} {result}")
