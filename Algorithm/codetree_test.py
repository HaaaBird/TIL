def cnt_move(si, sj, cnt):
    global result
    result = max(result, cnt)
    di = delta[move_dir[si][sj] - 1]
    for m in range(1, N):
        ni = si + di[0] * m
        nj = sj + di[1] * m
        if 0 <= ni < N and 0 <= nj < N and num[si][sj] < num[ni][nj]:
            cnt_move(ni, nj, cnt + 1)
    return



N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
move_dir = [list(map(int, input().split())) for _ in range(N)]
R, C = map(int, input().split())
R -= 1
C -= 1
delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
result = 0
cnt_move(R, C, 0)
print(result)

# Please write your code here.
