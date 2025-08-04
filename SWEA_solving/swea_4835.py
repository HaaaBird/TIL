
def bubble_sort(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_arr = []
    for i in range(N - M + 1):
        now_sum = 0
        for j in range(M):
            now_sum += arr[i+j]
        sum_arr.append(now_sum)

    print(f"#{case+1} {max(sum_arr) - min(sum_arr)}")