# swea_5205.py
# 퀵 정렬

def quick_sort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quick_sort(a, l, s - 1)
        quick_sort(a, s + 1, r)
    return a


def partition(arr, l, r):
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)
    print(f"#{case} {arr[N//2]}")