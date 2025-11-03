# boj_11399.py
# ATM

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
sum_ = arr[0]
for i in range(1, N):
    arr[i] = arr[i-1] + arr[i]
print(sum(arr))
