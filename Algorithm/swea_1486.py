# swea_1486.py
# 장훈이의 선반
def backt(a, n_len, start):
    global result
    if B <= n_len:
        if n_len < result:
            result = n_len
        return
    if result < n_len:
        return
    if result - B == 0:
        return

    for i in range(start, N):
        a.append(i)
        backt(a, n_len + arr[i], i + 1)
        a.pop()


T = int(input())
for case in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 10 ** 9
    backt([], 0, 0)
    print(f"#{case} {result - B}")
