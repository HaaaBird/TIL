# swea_1219.py
# 길찾기

"""

전형적인 길찾기.
단방향 그래프
A = 0 B = 99 로 고정

간선이 몇개인지 이야기를 안하는데, 별거 없어 보인다. 그냥 dfs로 풀면 될듯?


"""


def DFS(start, end, tree):
    stack = [start]
    visits = set()

    while len(stack) != 0:
        now = stack.pop()
        if now == end:
            return 1
        if now not in visits:
            visits.add(now)
            child = tree[now]
            if len(child) != 0:
                for ch in range(len(child) - 1, -1, -1):
                    stack.append(child[ch])
    return 0


T = 10

for _ in range(1, T + 1):
    start = 0
    end = 99
    case, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree_map = [[] for _ in range(100)]
    for i in range(0, len(arr), 2):
        tree_map[arr[i]].append(arr[i + 1])

    result = DFS(start, end, tree_map)
    print(f"#{case} {result}")
