# swea_16531.py
# 이진 힙


def enq(n):
    global last, heap
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


def parents_sum(n):
    global heap
    result = 0
    p = n // 2
    while p > 0:
        result += heap[p]
        p = p // 2
    return result


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * 1000001
    last = 0
    for data in arr:
        enq(data)
    print(f"#{case} {parents_sum(last)}")
