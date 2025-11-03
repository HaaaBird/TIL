# swea_5204.py
# 병합 정렬
def marge_sort(arr):
    global result
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        marge_sort(left_arr)
        marge_sort(right_arr)
        if left_arr[-1] > right_arr[-1]:
            result += 1

        left_arr_idx = 0
        right_arr_idx = 0
        arr_idx = 0

        while left_arr_idx < len(left_arr) and right_arr_idx < len(right_arr):
            if left_arr[left_arr_idx] < right_arr[right_arr_idx]:
                arr[arr_idx] = left_arr[left_arr_idx]
                left_arr_idx += 1
            else:
                arr[arr_idx] = right_arr[right_arr_idx]
                right_arr_idx += 1
            arr_idx += 1
        while left_arr_idx < len(left_arr):
            arr[arr_idx] = left_arr[left_arr_idx]
            left_arr_idx += 1
            arr_idx += 1
        while right_arr_idx < len(right_arr):
            arr[arr_idx] = right_arr[right_arr_idx]
            right_arr_idx += 1
            arr_idx += 1


T = int(input())
for case in range(1, T + 1):
    result = 0
    N = int(input())
    arr = list(map(int, input().split()))
    marge_sort(arr)

    print(f"#{case} {arr[N//2]} {result}")