# boj_11659.py
# 구간 합 구하기4


import sys
# input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = []
all_sum = arr[0]
for i in range(N):
    all_sum += arr[i]
    arr_sum.append(all_sum)

print(arr_sum)

