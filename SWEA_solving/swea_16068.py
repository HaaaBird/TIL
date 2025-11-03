# swea_16068.py

def min_max(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[-1], arr[0]


if __name__ == "__main__":
    T = int(input())

    for case in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        max, min = min_max(arr, N)
        print(f"#{case+1} {max - min}")