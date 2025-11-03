# boj_15666.py
# n과 m 12


def dfs(num, depth):
    if depth == M:
        print(" ".join(map(str, a)))
        return

    for i in range(arr.index(num), n):
        a.append(arr[i])
        dfs(arr[i], depth + 1)
        a.pop()

visited = set()
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))
n = len(arr)
a = []

dfs(arr[0], 0)