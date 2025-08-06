# boj_2667.py
# 단지 번호 붙이기


N = int(input())
arr = []
for _ in range(N):
    arr.append([int(a) for a in input()])

di = [0, 1, 0, -1]
dj = [1,0,-1,0]
visit = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            pass
        else:
            for c in range(4):
                ni = i + di[c]
                nj = j + dj[c]
                if 0 <= ni < N and 0 <= nj < N and [ni, nj] not in visit:
                    

