# swea_2817.py


def backt(a, n, m, n_sum, start):
    global result
    if n_sum == m:
        result += 1
        return
    if n_sum > m:
        return
    for i in range(start, n):
        if i not in a:
            a.append(i)
            backt(a, n, m, n_sum + arr[i], i + 1)
            a.pop()

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    backt([], N, M, 0, 0)
    print(result)