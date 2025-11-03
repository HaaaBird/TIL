# boj_9465.py
# 스티커

"""
스티커 길이가 3인 시점부터
이전 선택에 따라 고를 수 있는 선택이 제한적임
"""
import sys
input = sys.stdin.readline
T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    # 스티커 길이가 1, 2일땐 그냥 때려잡기
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if N == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    # 길이가 2
    dp[0][1] = dp[1][0] + arr[0][1]
    dp[1][1] = dp[0][0] + arr[1][1]
    if N == 2:
        print(max(dp[0][1], dp[1][1]))
        continue
    # 길이가 3 이상
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i]

    print(max(dp[0][-1], dp[1][-1]))