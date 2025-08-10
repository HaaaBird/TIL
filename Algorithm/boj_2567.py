# boj_2567.py
# 색종이2

# 전체 탐색을 하는데, 상하좌우 델타로 확인해 봤을떄 1개라도 0이 있으면 외곽. 해당하면 + 처리


import sys
input = sys.stdin.readline

N = int(input())
matrix = [[0] * 100 for _ in range(100)]
papers = [tuple(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for paper in papers:
    for i in range(paper[1], paper[1]+10):
        for j in range(paper[0], paper[0]+10):
            matrix[i][j] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] != 0:
            for c in range(4):
                ni = i + di[c]
                nj = j + dj[c]
                if 0 <= ni < 100 and 0 <= nj < 100:
                    if matrix[ni][nj] == 0:
                        cnt += 1
                else:
                    cnt += 1

print(cnt)

