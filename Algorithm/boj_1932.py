# boj_1932.py


N = int(input())
dp = []

if N == 1:
    print(int(input()))
else:
    for i in range(N):
        arr = list(map(int, input().split()))
        if i == 0:
            dp = arr[:]
        else:
            next_dp = []
            for k in range(len(arr)):
                if k == 0: # 시작 노드면
                    next_dp.append(dp[0] + arr[0])
                elif k == len(arr) - 1: #마지막 노드면
                    next_dp.append(dp[-1] + arr[-1])
                else:
                    next_dp.append(max(dp[k-1] + arr[k], dp[k] + arr[k]))
            dp = next_dp
    print(max(dp))
