# boj_17404.py
# 맨앞, 맨뒤 빼고 일단 dp계산


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
DP = [[[] for _ in range(3)] for _ in range(N)]
DP[0][0].append(matrix[0][0])
DP[0][1].append(matrix[0][1])
DP[0][2].append(matrix[0][2])

DP[1][0].append(matrix[0][0])
DP[1][1].append(matrix[0][1])
DP[1][2].append(matrix[0][2])

print(DP)

for i in range(2, N - 1):
    DP[i][0].append() = min()
    pass