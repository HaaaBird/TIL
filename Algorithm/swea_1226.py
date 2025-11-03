# swea_1226.py
# 미로
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = 10
for case in range(1, T + 1):
    tc = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(16)]
    s_ni = None
    e_ni = None
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                s_ni = (i, j)
            elif matrix[i][j] == 3:
                e_ni = (i, j)

    queue = [(s_ni[0], s_ni[1])]
    visits = set()
    flag = False

    while len(queue) != 0 and not flag:
        i, j = queue.pop(0)
        visits.add((i, j))
        for k in range(4):
            ni = i + delta[k][0]
            nj = j + delta[k][1]
            if 0 <= ni < 16 and 0 <= nj < 16 and (ni, nj) not in visits:
                if matrix[ni][nj] == 3:
                    flag = True
                    break
                elif matrix[ni][nj] == 0:
                    queue.append((ni, nj))
    if flag:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")