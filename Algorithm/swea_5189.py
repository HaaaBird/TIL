# swea_5189.py
# 전자카트

"""
인접 리스트로 코스트가 주어진다.
그냥 백트래킹으로 대충 풀면 풀릴듯?
백트래킹으로 순열 구해서 값 계산 돌리다가
최소보다 비싸면 컷 하는 방식으로 구현
"""


def backT(before, temp_score, arr, N):
    global result
    if len(arr) == N - 1: # 도달했다면
        temp_score += matrix[arr[-1]][0]
        result = min(result, temp_score)
    # 가지치기 길이에 도달하지 않았음에도 기존 min보다 높으면 return
    if temp_score > result:
        return
    for i in range(1, N): # 고정 출발위치인 1을 제외한 나머지 구하는 식
        if i not in arr:
            temp_score += matrix[before][i]
            arr.append(i)
            backT(i, temp_score, arr, N)
            temp_score -= matrix[before][i]
            arr.pop()


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 10 ** 9
    backT(0,0,[],N)
    print(f"#{case} {result}")

