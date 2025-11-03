# boj_24446.py
# 너비 우선 탐색3

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visit = [-1] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = [R]
visit[R] = 0
head = 0

while head < len(queue):
    now = queue[head]
    head += 1
    for child in graph[now]:
        if visit[child] == -1:
            visit[child] = visit[now] + 1
            queue.append(child)

for i in range(1, N + 1):
    print(visit[i])