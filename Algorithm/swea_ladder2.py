# swea_ladder2.py
# 사다리 다시풀기


for _ in range(10):
    N = 10
    cn = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ni = N - 1
    nj = arr[N-1].index(2)
    visit = set()
    di = [0, 0, -1] # right, left, up
    dj = [1, -1, 0]

    while ni > 0:
        for c in range(3):
            ni += di[c]
            nj += dj[c]
            if 0 <= nj < N and (ni,nj) not in visit and arr[ni][nj] == 1:
                visit.add((ni,nj))
                break
            else:
                ni -= di[c]
                nj -= dj[c]
    print(f'#{cn} {nj}')