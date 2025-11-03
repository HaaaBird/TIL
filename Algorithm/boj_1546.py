# boj_1546.py
# 평균 구하기

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
my_max = max(nums)
n_sum = sum(nums)
print(n_sum * 100 / my_max / N)