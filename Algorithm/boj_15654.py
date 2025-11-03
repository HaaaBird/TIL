# boj_15654.py
# N과 M (5)
"""
이 전엔 수열이 없었는데 이젠 생김.
오름차순 강요됨으로 그냥 sort 써서 풀면 될듯?
"""

def backtrack(arr, n, m):
    global in_arr
    if len(arr) == m:
        print(*arr)
        return
    for i in range(n):
        if in_arr[i] not in arr:
            arr.append(in_arr[i])
            backtrack(arr, n, m)
            arr.pop()

N, M = map(int, input().split())
in_arr = list(map(int, input().split()))
in_arr.sort()

backtrack([], N, M)