# swea_5688.py
# 세제곱근 찾아라
"""
이진 탐색으로 0~N 사이 구간값 가지고 해 보다가 없으면 -1 출력
"""

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    start = 0
    end = min(N, 10**6)
    result = -1
    while start <= end:
        mid = (start + end) // 2
        n_val = pow(mid, 3)
        if n_val == N:
            result = mid
            break
        elif n_val < N: # 작다면
            start = mid + 1
        else:
            end = mid - 1

    print(f"#{case} {result}")
