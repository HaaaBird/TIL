T = int(input())
for case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_fall = 0
    for i in range(N):
        drop = 0
        for j in range(i+1, N):
            if arr[i] > arr[j] : drop += 1
        if max_fall < drop: max_fall = drop
    print(f"#{case+1} {max_fall}")