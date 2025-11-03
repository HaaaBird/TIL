# swea_16261.py
# 부분집합의 합

T = int(input())

for case in range(1, T + 1):
    arr = list(map(int, input().split()))
    s_flag = False
    for i in range(1 << 10):
        now_sum = 0
        for j in range(len(arr)):
            if i & (1 << j):
                now_sum += arr[j]
        if now_sum == 0 and i != 0:
            s_flag = True
            break
    if s_flag:
        print(f"#{case} 1")
    else:
        print(f"#{case} 0")