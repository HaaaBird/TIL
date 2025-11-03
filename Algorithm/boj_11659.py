# boj_11659.py
# 구간 합 구하기4


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
all_sum = 0
arr_sum = []

for i in range(N):
    all_sum += arr[i]
    arr_sum.append(all_sum)

for case in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(arr_sum[end-1])
    else:
        result = arr_sum[end-1] - arr_sum[start - 2]
        print(result)

