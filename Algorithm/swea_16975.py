# swea_16975.py
# 6일차 그룹 나누기
from collections import deque

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = {}
    visited = set()

    for i in range(0, len(arr), 2):
        A, B = arr[i], arr[i+1]
        if graph.get(A):
            graph[A].append(B)
        else:
            graph.update({A:[B]})
        if graph.get(B):
            graph[B].append(A)
        else:
            graph.update({B:[A]})
    result = 0
    for i in range(1, N + 1):
        if i not in visited:
            queue = deque([(i, 0)])
            visited.add(i)
            result += 1
            while len(queue) != 0:
                now, d = queue.pop()
                if graph.get(now):
                    for n_node in graph[now]:
                        if n_node not in visited:
                            queue.append((n_node, d + 1))
                            visited.add(n_node)
    print(f"#{case} {result}")