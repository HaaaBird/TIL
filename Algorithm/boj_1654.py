# boj_1654.py
# 랜선 자르기
import sys
input = sys.stdin.readline

def get_cnt(arr, dist):
    cnt = 0
    for val in arr:
        cnt += val // dist
    return cnt

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

start = 1
end = max(cables)
result = 0
while start <= end:
    mid = (start + end) // 2
    n_result = get_cnt(cables, mid)
    if n_result >= N:
        result = max(result, mid)
        start = mid + 1
    elif n_result < N:
        end = mid - 1

print(result)
