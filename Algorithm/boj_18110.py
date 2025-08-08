# boj_18110.py
# Solved.AC
import math

N = int(input())
if N == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(N)]
    arr.sort()
    a = int(N * 0.15 + 0.5)
    result_list = arr[a:N - a]
    print(round(sum(result_list) / (N - a * 2)))
