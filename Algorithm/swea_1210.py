# swea_1210.py
# 사다리타기
for case in range(1,11):
    T = int(input())
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 0, -1] # right, left, up
    dj = [1, -1, 0]
    nj = 0
    # 아래에서 올라가는 형태로 구현
    for i in range(N):
        if matrix[-1][i] == 2:
            nj = i
    ni = N-1
    visit = set()
    while True:
        if ni == 0:
            break
        for c in range(3):
            ni += di[c]
            nj += dj[c]
            if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 1 and (ni, nj) not in visit:
                visit.add((ni, nj))
                break
            else:
                ni -= di[c]
                nj -= dj[c]

    print(f"#{T} {nj}")