import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

used_sum = [False] * (2*N)          # i+j
used_diff = [False] * (2*N)         # i-j + (N-1)

def dfs(start_s, cnt):
    global best
    if start_s >= 2*N - 1:
        if cnt > best:
            best = cnt
        return

    s = start_s

    # 이 대각선(s)에서 비숍을 하나 놓아보는 모든 경우
    for i in range(N):
        j = s - i
        if 0 <= j < N and board[i][j] == 1:
            si = i + j
            di = i - j + (N - 1)
            if not used_sum[si] and not used_diff[di]:
                used_sum[si] = used_diff[di] = True
                dfs(s + 2, cnt + 1)
                used_sum[si] = used_diff[di] = False

    # 이 대각선에서 아무 것도 안 놓는 선택(필수 분기)
    dfs(s + 2, cnt)

# 검은 칸(짝수 s) 최대
best = 0
dfs(0, 0)
black_max = best

# 흰 칸(홀수 s) 최대
best = 0
dfs(1, 0)
white_max = best

print(black_max + white_max)
