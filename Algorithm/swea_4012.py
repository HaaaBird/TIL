# swea_4012.py
# 요리사


def find(arr, start):
    global result
    if len(arr) == N // 2:
        food1 = 0
        food2 = 0
        # 음식 1번 계산
        for i in range(N):
            for j in range(N):
                if i in arr and j in arr:
                    # 음식 1번
                    food1 += graph[i][j]
                elif i not in arr and j not in arr:
                    # 음식 2번
                    food2 += graph[i][j]
        diff = abs(food1 - food2)
        result = min(result, diff)
        return

    for i in range(start, N):
        if i not in arr:
            arr.append(i)
            find(arr, i)
            arr.pop()

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    result = 10**21
    find([], 0)
    print(f"#{case} {result}")
