# boj_1920.py
# 수 찾기

import sys

input = sys.stdin.readline


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


def b_search_2(arr, low, high, target):
    if low > high:  # 검색 실패
        return False
    else:
        mid = (high + low) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            return b_search_2(arr, low, mid - 1, target)
        else:
            return b_search_2(arr, mid + 1, high, target)


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
target_arr = list(map(int, input().split()))

for i in range(M):
    result = b_search_2(arr, low=0, high=(len(arr) - 1), target=target_arr[i])
    print(int(result))
