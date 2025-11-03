# swea_5207.py
# 이진 탐색

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    A.sort()
    for target in B: # 아래 열을 타겟으로 잡아서 검색
        start = 0
        end = N - 1
        find = False
        lst_dir = 0

        while start <= end:
            mid = (start + end) // 2
            if target == A[mid]:
                find = True
                break
            elif target > A[mid]: # 중간보다 타겟이 더 크다
                if lst_dir == 1: # 이전에도 오른쪽으로 이동한거라면
                    break
                start = mid + 1
                lst_dir = 1
            else: # 타겟이 중간보다 작다.
                if lst_dir == -1: # 이전에도 왼쪽으로 이동한거라면
                    break
                end = mid - 1
                lst_dir = -1
        if find:
            result += 1
    print(f"#{case} {result}")

