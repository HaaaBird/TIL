# boj_2798.py
# 블랙잭 기본
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            n_sum = arr[i] + arr[j] + arr[k]
            if n_sum == M:
                result = arr[i] + arr[j] + arr[k]
                break
            elif n_sum > M:
                pass
            elif M - n_sum < M - result:
                result = n_sum
print(result)
