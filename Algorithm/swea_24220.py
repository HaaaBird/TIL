# swea_24220.py
# 경로의 수


def find(s_idx):
    global result
    if s_idx == target:
        result += 1
        return

    if graph.get(s_idx):
        for node in graph[s_idx]:
            if node not in visited:
                visited.add(node)
                find(node)
                visited.remove(node)


T = int(input())
for case in range(1, T + 1):
    N, E = map(int, input().split())
    arr = list(map(int, input().split()))
    start, target = map(int, input().split())
    graph = {}
    result = 0
    for i in range(0, len(arr), 2):
        if graph.get(arr[i]):
            graph[arr[i]].append(arr[i + 1])
        else:
            graph.update({arr[i]: [arr[i + 1]]})
    visited = {start}

    find(start)
    print(f"#{case} {result}")
