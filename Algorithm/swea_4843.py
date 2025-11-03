# swea_4843.py
# 약간 특별한 정렬
def selection_sort(arr):
    for i in range(len(arr)):
        max_idx = i
        min_idx = i
        if i % 2 == 0:
            for j in range(i + 1, len(arr)):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


T = int(input())
for case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    selection_sort(arr)
    print(f"#{case + 1}", end=" ")
    for i in range(10):
        print(arr[i], end=" ")
    print()
