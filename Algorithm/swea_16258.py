# swea_16258.py
# 델타 문제

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    all_sum = 0
    for i in range(N):
        for j in range(N):
            for c in range(4):
                ni = i + di[c]
                nj = j + dj[c]
                if 0 <= ni < N and 0 <= nj < N:
                    result = arr[ni][nj] - arr[i][j]
                    if result < 0: result *= -1
                    all_sum += result
    print(f"#{case} {all_sum}")
