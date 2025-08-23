import time
import random
import math


def marge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        marge_sort(left_arr)
        marge_sort(right_arr)

        left_idx = 0
        right_idx = 0
        arr_idx = 0
        while left_idx < len(left_arr) and right_idx < len(right_arr):
            if left_arr[left_idx] < right_arr[right_idx]:
                arr[arr_idx] = left_arr[left_idx]
                left_idx += 1
            else:
                arr[arr_idx] = right_arr[right_idx]
                right_idx += 1
            arr_idx += 1

        while left_idx < len(left_arr):
            arr[arr_idx] = left_arr[left_idx]
            left_idx += 1
            arr_idx += 1

        while right_idx < len(right_arr):
            arr[arr_idx] = right_arr[right_idx]
            right_idx += 1
            arr_idx += 1


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def counting_sort(arr, N):
    c_arr = [0] * (N + 1)
    for i in range(len(arr)):
        c_arr[arr[i]] += 1
    result = []
    for i in range(len(c_arr)):
        if c_arr[i] != 0:
            for j in range(c_arr[i]):
                result.append(i)


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        m_idx = i
        for j in range(n):
            if arr[j] < arr[m_idx]:
                m_idx = j
        arr[i], arr[m_idx] = arr[m_idx], arr[i]


if __name__ == "__main__":
    N = 100_000 # 10만개
    N_range = 1_000 # 숫자의 범위는 1~1000
    arr = [random.randint(1, N_range) for _ in range(N)]

    # 머지 정렬
    start = time.time()
    marge_sort(arr[:])
    end_time = time.time()
    print("합병정렬 시간:", round(end_time - start, 6))

    # 카운팅정렬
    start = time.time()
    counting_sort(arr[:], N_range)
    end_time = time.time()
    print("카운팅정렬 시간:", round(end_time - start, 6))

    # 파이썬 내장 정렬
    start = time.time()
    arr[:].sort()
    end_time = time.time()
    print("내장정렬 시간:", round(end_time - start, 6))

    # 선택정렬
    start = time.time()
    selection_sort(arr[:])
    end_time = time.time()
    print("선택정렬 시간:", round(end_time - start, 6))

    # 버블정렬
    start = time.time()
    bubble_sort(arr[:])
    end_time = time.time()
    print("버블정렬 시간:", round(end_time - start, 6))
