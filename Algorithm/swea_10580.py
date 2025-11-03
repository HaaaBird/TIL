# swea_10580.py
# 전봇대

"""
새로운 선의
시작점이 기존 선의 시작보다 높고
도착점이 기존 선의 도착보다 낮음

시작점이 기존 선의 시작보다 낮고
도착점이 기존 선의 도착보다 낮음.
"""
T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        n = matrix[i]
        for j in range(i+1, N):
            if n[0] > matrix[j][0] and n[1] < matrix[j][1]:
                result += 1
            elif n[0] < matrix[j][0] and n[1] > matrix[j][1]:
                result += 1

    print(f"#{case} {result}")