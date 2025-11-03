# boj_15657.py
# N과 M(7)


"""
비내림차순, 유사 조합

"""

def backt(arr, start, n, m):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start, n):
        arr.append(in_arr[i])
        backt(arr, i, n, m)
        arr.pop()


N,M = map(int, input().split())
in_arr = list(map(int, input().split()))
in_arr.sort()
backt([], 0, N, M)
